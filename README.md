# Build the docker network and nginx proxy

```bash
docker network create dockernetwork
docker build -t rlcosta121/test-app .
docker run -d -p 5000:5000 --name test-app rlcosta121/test-app
docker network connect dockernetwork test-app
docker build -t rlcosta121/nginx-proxy .
docker run -d --name nginx-proxy -p 80:80 --network dockernetwork rlcosta121/nginx-proxy
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
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
