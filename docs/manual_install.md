# Manual Installation

## Prerequisite

- Kubernetes cluster >= v1.17


## Install
### Argo workflow and CLI
Please see [Argo Quickstart](https://github.com/argoproj/argo/blob/master/README.md#Quickstart) and
get [Argo CLI](https://github.com/argoproj/argo/releases/tag/v2.12.3).


### Argo CD
Please see [Argo CD Quickstart](https://argoproj.github.io/argo-cd/getting_started/).


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
lma
lma-federation
service-mesh
openstack-components
openstack-infra
```

Run Workflow and check your argo UI.
```console
$ argo submit --from wftmpl/lma-federation -nargo
```
