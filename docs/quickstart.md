# Quick Start
This document is a quick guide to install `argo` and `decapod-flow`.

## Prerequisite
* kubernetes cluster >= v1.17
* Available [Storage Classes](https://kubernetes.io/docs/concepts/storage/storage-classes/) in Kubernetes for the workflow archiving

## Prepare

[Tacoplay](https://github.com/openinfradev/tacoplay) is a set of ansible playbooks including `decapod` playbook which install components of `decapod`.  

Please refer to the details at [Tacoplay install guide](https://taco-docs.readthedocs.io/ko/latest/intro/aio-k8s.html#installing-guide).  

### Prepare tacoplay
  ```console
  git clone https://github.com/openinfradev/tacoplay.git

  cd tacoplay && ./fetch_sub-projects.sh

  sudo pip install -r requirements.txt --upgrade --ignore-installed

  sudo pip install --upgrade pip
  ```

### Write inventory files  
  1. tacoplay/inventory/test/hosts.ini
      ```yaml
      master-node access_ip=127.0.0.1 ansible_connection=local 
      
      [admin-node]
      master-node
      ```
  2. tacoplay/inventory/test/extra-vars.yml
      ```yaml
      taco_storageclass_name: "" # storage class name      
      ```

## Install
```console
# Run commands inside tacoplay directory
ansible-playbook -b -i inventory/test/hosts.ini -e @inventory/test/extra-vars.yml site.yml --tags decapod --skip-tags ceph,k8s
```

## Usage
After completion of installation, node port 30004 is open. Please access to http://master-node-ip:30004 .  
Then explore and make fun with workflows!