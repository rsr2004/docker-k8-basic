## Running the project on Kubernetes

- inside the k8-deployment-files folder
```sh
./run-kube.sh
kubectl apply -f <yaml-file-name> 
```

---

# removing components in k8s
```bash
kubectl delete <service/deployment>
kubectl delete all --all --all-namespaces
```

---

# troubleshoot
- kubectl logs <pod-name>

---

## TEMP

 # Create a new TLS secret named tls-secret with the given key pair
  kubectl create secret tls tls-secret --cert=path/to/tls.crt --key=path/to/tls.key

curl -I http://cert.rlcosta.cloudns.ch

kubectl describe pods

