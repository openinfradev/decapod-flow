#!/usr/bin/python3

import argparse
import git
import ruamel.yaml
import os
import sys

print("Entering updateEndpoint script..")

parser = argparse.ArgumentParser()
parser.add_argument('--action', required=True, type=str,
            help="action to take: 'add' or 'delete'")
parser.add_argument('--cluster_name', required=True, type=str,
            help="cluster name to which the endpoint is added")
parser.add_argument('--endpoint', required=True, type=str,
            help="endpoint to add")

args = parser.parse_args()
action = args.action
clusterName = args.cluster_name
endpoint = args.endpoint
repo = None
config = {}
commit_msg = ''

sitePath = './decapod-site'
siteFileName = "{}/lma/site-values.yaml".format(clusterName)
siteFileNameFull = "{}/{}".format(sitePath, siteFileName)

# Clone or re-use decapod-site repository #
if not os.path.isdir(sitePath):
    print("Cloning repository...")

    repo = git.Repo.clone_from('https://github.com/robertchoi80/decapod-site', 'decapod-site')
    with repo.config_writer() as git_config:
        git_config.set_value('user', 'email', 'tks-argo@tks.com')
        git_config.set_value('user', 'name', 'TKS Argo')
else:
    repo = git.Repo(sitePath)
    repo.remotes.origin.pull()

with open(siteFileNameFull, 'r') as f:
    config = ruamel.yaml.round_trip_load(f, preserve_quotes=True)

charts = config["charts"]
thanosChart = [chart for chart in charts if chart['name'] == "thanos"][0]

if action == 'add':
    if (endpoint in thanosChart['override']['querier.stores']):
        print("The endpoint already exists.")
        sys.exit(0)
    else:
        #print("Before insertion: {}".format(thanosChart))
        thanosChart['override']['querier.stores'].append(endpoint)
        #print("After insertion: {}".format(thanosChart))
        commit_msg = "add new thanos-sidecar endpoint to '{}' cluster".format(clusterName)
elif action == 'delete':
    if (endpoint in thanosChart['override']['querier.stores']):
        print("Found endpoint. Deleting it...")
        thanosChart['override']['querier.stores'].remove(endpoint)
        commit_msg = "delete thanos-sidecar endpoint from '{}' cluster".format(clusterName)
    else:
        print("The endpoint {} doesn't exist. Exiting script...".format(endpoint))
        sys.exit(0)
else:
    sys.exit("Wrong action type")

with open(siteFileNameFull, 'w') as f:
    ruamel.yaml.round_trip_dump(config, f)

diff = repo.git.diff(repo.head.commit.tree)
print(diff)

# Provide a list of the files to stage
repo.index.add([siteFileName])

# Provide a commit message
repo.index.commit(commit_msg)
res = repo.remotes.origin.push()[0]

# flag '256' means successful fast-forward
if res.flags != 256:
    print(res.summary)
    sys.exit("Push failed!")

print("Exiting updateEndpoint script..")
