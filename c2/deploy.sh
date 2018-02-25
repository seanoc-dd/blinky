#!/bin/bash

set -e

function usage()
{
    echo "Script used for pushing new code out."
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

gcloud container builds submit --tag gcr.io/blinky-196302/c2-image:v$VERSION
kubectl --cluster=gke_blinky-196302_us-east1-b_home set image deployment/c2-server c2-server=gcr.io/blinky-196302/c2-image:v$VERSION
