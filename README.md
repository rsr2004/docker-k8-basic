# Running the project on Docker only

build the images and network
```bash
docker network create dockernetwork
docker build -t <app-name> .
```

running the images
```bash
docker run -d -p 7070:8080 --network dockernetwork --name plik-app rlcosta121/plik-app
docker run -d -p 5050:  --network dockernetwork --name
docker run -d -p 6060:  --network dockernetwork --name
docker-compose up -d (for docker-compose apps)
docker run -d --name nginx-proxy -p 80:80 -p 443:443 --network dockernetwork rlcosta121/nginx-proxy
```
---

# Build the docker network and nginx proxy

```bash
docker network create dockernetwork
docker build -t rlcosta121/plik-app .
docker run -d -p 7070:8080 --network dockernetwork --name plik-app rlcosta121/plik-app
docker build -t rlcosta121/nginx-proxy .
docker run -d --name nginx-proxy -p 80:80 -p 443:443 --network dockernetwork rlcosta121/nginx-proxy

docker exec nginx-proxy nginx -s reload
docker restart <container-name>

docker network connect dockernetwork <container-name>
```
---

# Pruning

```bash
docker rm $(docker ps -aq)
docker rmi <image_name_or_id1> <image_name_or_id2> <image_name_or_id3>
docker image prune -a
docker container prune -a
docker system prune
docker system df -v <- check for remenants
```
---

# troubleshoot
docker logs <container-name>
docker network inspect <network_name>

---

# Tools used

- ejbca-ce
- plik
- wikijs
- onetime secret
- dynu.com
- cloudns
