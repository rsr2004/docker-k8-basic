#!/bin/bash

kubectl apply -f pv.yaml

sleep3
kubectl apply -f pvc.yaml

sleep 3
kubectl apply -f postgres-deployment.yaml

sleep 3
kubectl apply -f plik-deployment.yaml

sleep 3
kubectl apply -f wiki-deployment.yaml

sleep 3
kubectl apply -f secret-deployment.yaml

sleep 3
kubectl apply -f ejbca-deployment.yaml

sleep 3
kubectl apply -f nginx-configmap.yaml

sleep 3
kubectl apply -f nginx-deployment.yaml

