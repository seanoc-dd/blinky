#!/bin/bash

POPS=(
    "us-west1-a"
)

set -e

TAG="v-`git rev-parse --short HEAD`"

gcloud container builds submit --tag gcr.io/blinky-196302/pop-image:$TAG
for POP in ${POPS[@]}; do
    echo "Updating $POP to v$VERSION"
    CLUSTER_NAME="pop-$POP"
    K8S_CLUSTER_NAME="gke_blinky-196302_"$POP"_$CLUSTER_NAME"

    kubectl  --cluster=$K8S_CLUSTER_NAME set image deployment/pop-process pop-process=gcr.io/blinky-196302/pop-image:$TAG

done
