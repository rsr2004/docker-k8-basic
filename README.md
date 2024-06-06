# Build the docker network and nginx proxy

```bash
docker network create dockernetwork
docker build -t rlcosta121/test-app .
docker run -d -p 5000:5000 --name test-app rlcosta121/test-app
docker network connect dockernetwork test-app
docker build -t rlcosta121/nginx-proxy .
docker run -d --name nginx-proxy -p 80:80 --network dockernetwork rlcosta121/nginx-proxy
```


## Tools used

- ejbca-ce
- plik
- wikijs
- onetime secret
- dynu.com
