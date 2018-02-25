# Blinky
![Blinky](https://vignette.wikia.nocookie.net/simpsons/images/b/b0/250px-Blinky.png/revision/latest)

Blinky is a proof of concept for a geo-distibuted synthetic testing and monitoring service.

For a detailed background on the goals of the larger synthetic testing project, checkout the [RFC](https://docs.google.com/document/d/1JCnzFIHx-3n7vhvJKSORUh0kCF8hps1aamhP3wpP1sA/edit#).

## Prereqs

This project is setup to run on GCP using kubernetes engine. Accordingly, you'll need a GCP project setup and the gcloud cli tools installed on your machine.

```
gcloud init
gcloud components install kubectl
glcoud config set project blinky-196302
```

Note: replace `blinky-196302` with whatever your GCP project id is.


## C2
Command and Control

This is the service that manages POPs and tests.

### Initial deployment

```
cd c2
gcloud container clusters create home
gcloud container clusters get-credentials home
gcloud container builds submit --tag gcr.io/blinky-196302/c2-image
kubectl create secret generic cloudsql-db-credentials --from-literal=username=proxyuser --from-literal=password="$DBPASS"
kubectl create secret generic cloudsql-instance-credentials  --from-file=credentials.json=credentials.json
kubectl create -f deployment.yaml

kubectl get service c2-server
```

You might need to wait a few minutes but eventually you should be able to run `kubectl get service c2-server` and get a public address you can hit in a web browser to see the c2 interface.

### Deploy Updates

1. Increment the `v#` value on line 3 of `c2/cloudbuild.yaml`
2. `gcloud container builds submit --config cloudbuild.yaml .`
3. `kubectl --cluster=gke_blinky-196302_us-east1-b_home set image deployment/c2-server c2-server=gcr.io/blinky-196302/c2-image:v#` Replacing `#` with the number set in step 1


### Scaling

`kubectl scale deployment c2-server --replicas=3`


### Shutdown & Cleanup

```
kubectl delete service c2-server
gcloud container clusters delete home
```

## POPs

POPs are the geo-distibuted clusters from which tests are run.

### Launching new POPs

1. Create a new file in the deployments directory similar to the existing files, for the new zone.
2. Go to http://blinky.seanoc.com/admin/ and add a new POP entry for the new zone.
3. Run `./launch_new_pop --zone=$ZONE`


### Deploying to POPs

1. Increment the version number on line 3 of `pops/cloudbuild.yaml`.
2. `gcloud container builds submit --config cloudbuild.yaml .`
3. `./deploy.sh --version=$VERSION` where `$VERSION` is the number you set in step 1.
