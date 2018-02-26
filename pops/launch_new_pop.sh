#!/bin/bash

set -e

function usage()
{
    echo "Script used for launching new POPs"
    echo ""
    echo "./launch_new_pop.sh"
    echo "\t-h --help"
    echo "\t--zone=$ZONE"
    echo "\t--location-name=$LOCATION_NAME"
    echo ""
}

while [ "$1" != "" ]; do
    PARAM=`echo $1 | awk -F= '{print $1}'`
    VALUE=`echo $1 | awk -F= '{print $2}'`
    case $PARAM in
        -h | --help)
            usage
            exit
            ;;
        --zone)
            ZONE=$VALUE
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done

CLUSTER_NAME="pop-$ZONE"
K8S_CLUSTER_NAME="gke_blinky-196302_"$ZONE"_$CLUSTER_NAME"

gcloud container clusters --zone=$ZONE create $CLUSTER_NAME
gcloud container clusters --zone=$ZONE get-credentials "$CLUSTER_NAME"
kubectl --cluster=$K8S_CLUSTER_NAME create -f deployments/$ZONE.yaml
kubectl --cluster=$K8S_CLUSTER_NAME set image deployment/pop-process pop-process=gcr.io/blinky-196302/pop-image:$TAG
