#!/bin/bash

kubectl apply -f plik-deployment.yaml

sleep 3
kubectl apply -f nginx-configmap.yaml

sleep 3
kubectl apply -f nginx-deployment.yaml

sleep 3
kubectl apply -f wiki-deployment.yaml


#sleep 2
#curl "http://34.192.67.156:30001"
