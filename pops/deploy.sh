#!/bin/bash

POPS=(
    "us-west1-a"
)

set -e

function usage()
{
    echo "Script used for pushing new code out to all POPs."
    echo ""
    echo "./deploy.sh"
    echo "\t-h --help"
    echo "\t--version=$VERSION"
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
        --version)
            VERSION=$VALUE
            ;;
        *)
            echo "ERROR: unknown parameter \"$PARAM\""
            usage
            exit 1
            ;;
    esac
    shift
done

for POP in ${POPS[@]}; do
    echo "Updating $POP to v$VERSION"
    CLUSTER_NAME="pop-$POP"
    K8S_CLUSTER_NAME="gke_blinky-196302_"$POP"_$CLUSTER_NAME"

    kubectl  --cluster=$K8S_CLUSTER_NAME set image deployment/pop-process pop-process=gcr.io/blinky-196302/pop-image:v$VERSION

done
