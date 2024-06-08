# Running the project on Docker only
build the images and network
```bash
docker network create dockernetwork
docker build -t <app-name> .
```

running the images
```bash
docker run -d -p 7070:8080 --network dockernetwork --name plik-app rlcosta121/plik-app
docker run -d --name secret-app --network dockernetwork --network-alias secret-app -p 5050:5050 rlcosta121/secret-app
docker-compose up -d (for docker-compose apps)
docker run -d --name nginx-proxy -p 80:80 -p 443:443 --network dockernetwork rlcosta121/nginx-proxy
docker network connect dockernetwork <container-name>
```
---

```bash
docker exec nginx-proxy nginx -s reload
docker restart <container-name>
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
