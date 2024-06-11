# Running the project on Docker only
build the images and network
```sh
docker network create dockernetwork
docker build -t <app-name> .
```

running the images
```sh
docker run -d -p 7070:8080 --network dockernetwork --name plik-app --network-alias plik-app rlcosta121/plik-app
docker run -d --name secret-app --network dockernetwork --network-alias secret-app -p 5050:5050 rlcosta121/secret-app
docker run -d --name wiki-app --network dockernetwork --network-alias wiki-app -p 6060:3000 rlcosta121/wiki-app
docker run -d --name nginx-proxy -p 80:80 -p 443:443 --network dockernetwork rlcosta121/nginx-proxy
docker network connect dockernetwork <container-name>
```
---

```bash
docker exec nginx-proxy nginx -s reload
docker restart <container-name>
```
---

## Running the project on Kubernetes

- inside the k8-deployment-files folder
```sh
./nginx-deployment
./plik-deployment
./secret-deployment
./wiki-deployment
kubectl apply -f ejbca-deployment.yaml
```

---

# removing components
```bash
docker rm $(docker ps -aq)
docker rmi <image_name_or_id1> <image_name_or_id2> <image_name_or_id3>
docker image prune -a
docker container prune
docker system prune
docker system df -v <- check for remenants
```
---

# troubleshoot
- docker logs <container-name>
- docker network inspect <network_name>

---

# tools used
- ejbca-ce
- plik
- wikijs
- onetime secret
- dynu.com
- cloudns

---

# copy files from the container into the machine hosting them

```sh
docker exec -it plik-app [bash OR sh]
```
- identify where the file is located
- exit the container and run

```sh
docker cp <container-name>:path/to/file/on/container /path/on/local-host
scp -i <private-key> <instance-user>@<instance-ip>:/path/to/instance/file /path/in/local/machine
```

---

## Generating the certificates to enable ssl on cert.rlcosta.clodns.ch
1. Inside the nginx-proxy folder

```bash
# Generate a private key
openssl genrsa -out server.key 2048

# Generate a Certificate Signing Request (CSR)
openssl req -new -key server.key -out server.csr

# Generate a self-signed certificate
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```
This will generate server.key (private key) and server.crt (certificate).

2. copy the certificates into the container and expose ports(Dockerfile)
```bash
COPY server.crt /etc/nginx/server.crt
COPY server.key /etc/nginx/server.key

EXPOSE 443 80
```

3. redirect incoming requests into https on path /ejbca/adminweb 
- nginx.conf
```bash
server {
    listen 80;
    server_name cert.rlcosta.cloudns.ch;

    location / {
        rewrite ^/(.*)$ https://$server_name/ejbca/adminweb/$1 permanent;
    }
}

server {
    listen 443 ssl;
    server_name cert.rlcosta.cloudns.ch;

    ssl_certificate /etc/nginx/server.crt;
    ssl_certificate_key /etc/nginx/server.key;

    location /ejbca/adminweb {
        proxy_pass https://ejbca-app:8443;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```


## Errors

The Service "nginx-fixed-service" is invalid: 
* spec.ports[0].name: Required value
* spec.ports[1].name: Required value

- this indicates that the 'name' field is required for each port specified in the Service definition
- example:
```bash
  ports:
    - protocol: TCP
      port: 80
      targetPort: 80
      name: http
    - protocol: TCP
      port: 443
      targetPort: 443
      name: https
```

---

## TEMP

domain to lb ip
to
load balancer(network lb) 80 > 30080 | 443 > 30443
to
target group(ips | 30080 is worker port) 30080 > 80(container-port) | 30443 > 443(container-port)

------------------

nginx listen on port 80 and 443(nodePort:30080, 30443 in nginx-deployment.yaml | externalIPs: -lbIP dentro do service)
to
redirect to internal ports. ex: 8080, 5050, 3000, 8443
to



kubectl get namespaces
kubectl delete namespace <namespace-name>
