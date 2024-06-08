# Build the docker network and nginx proxy

```bash
docker network create dockernetwork
docker build -t rlcosta121/plik-app .
docker run -d -p 8081:8080 --network dockernetwork --name plik-app rlcosta121/plik-app
docker build -t rlcosta121/nginx-proxy .
docker run -d --name nginx-proxy -p 80:80 -p 443:443 --network dockernetwork rlcosta121/nginx-proxy

docker exec nginx-proxy nginx -s reload
docker restart <container-name>
docker network inspect <network_name>
docker container port plik-app


remove all containers -> docker rm $(docker ps -aq)
remove multiple docker images -> docker rmi <image_name_or_id1> <image_name_or_id2> <image_name_or_id3> ...
remove all unused images and containers -> docker image prune |  docker container prune


docker network connect dockernetwork <container-name>
```
---

# Wiki.js documentation

```bash
mkdir wikijs
cd wikijs
mkdir data
nano docker-compose.yml
```

## docker-compose configuration
```bash
version: '3'

services:
  wiki:
    image: requarks/wiki:2
    ports:
      - "2020:2020"
    environment:
      - DB_TYPE=sqlite
    volumes:
      - ./data:/var/wiki/data
```

```sh
docker-compose up -d
```

## troubleshoot
docker-compose logs process-name

---

## Tools used

- ejbca-ce
- plik
- wikijs
- onetime secret
- dynu.com
- cloudns
