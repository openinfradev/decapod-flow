# Manual Installation

## Prerequisite

- Kubernetes cluster >= v1.17


## Install
### Argo workflow and CLI
Please see [Argo Quickstart](https://github.com/argoproj/argo/blob/master/README.md#Quickstart) and
get [Argo CLI](https://github.com/argoproj/argo/releases/tag/v2.12.3).


### Helm Operator
Please see [Helm Operator Quickstart](https://github.com/fluxcd/helm-operator/blob/master/docs/get-started/quickstart.md).


### Workflow
Create workflow templates using `Argo CLI`.
```console
$ argo template create decapod-flow/templates/helm-operator/helmrelease-wftpl.yaml
```

Workflow template is created if template file is successfully submited.  
Also, you can check the workflow template in Argo UI.
```console
$ argo template list

NAME
helmrelease
```

Run Workflow and check your argo UI.
```console
$ argo submit decapod-flow/workflows/openstack-infra-wf.tpl
```
