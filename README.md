# Simple docker + k8s project

Project's goal:

- Four applications running in the k8s cluster as service type `CluserIP` 
- Nginx will forward requests to the apps based on their domain names
- Nginx is associated with an AWS loadbalancer, so the requests will allways pass through nginx
- The four apps have databases and paths associated with them for persistence


---

Instructions are inside docker-deployment-files and k8s-deployment-files
