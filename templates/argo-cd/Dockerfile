FROM alpine:3.14
RUN apk update && apk add --no-cache curl bash

WORKDIR /workspace
RUN curl -sSL -o /workspace/argocd https://github.com/argoproj/argo-cd/releases/download/v2.0.1/argocd-linux-amd64
RUN chmod +x /workspace/argocd
