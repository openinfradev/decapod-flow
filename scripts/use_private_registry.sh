#!/bin/bash

set -e

if [[ $# == 0 ]]; then
	echo "./$0 container_registry_url"
	exit 1
fi

REGISTRY=$1

for file in $(find . -name '*.yaml');do
	sed -i "s/docker\.io/${REGISTRY}/g" $file
	sed -i "s/k8s\.gcr\.io/${REGISTRY}/g" $file
done
