#!/bin/bash

set -e

TAG="v-`git rev-parse --short HEAD`"

gcloud container builds submit --tag gcr.io/blinky-196302/c2-image:$TAG
kubectl --cluster=gke_blinky-196302_us-east1-b_home set image deployment/c2-server c2-server=gcr.io/blinky-196302/c2-image:$TAG
