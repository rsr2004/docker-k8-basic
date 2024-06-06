# Build the docker network and nginx proxy

```bash
docker network create dockernetwork
cd nginx-proxy/
docker build -t rlcosta121/nginx-proxy . 
nano nginx.conf 
docker network connect bridge test-app
cd ..
cd test-app/
docker build -t rlcosta121/test-app
docker build -t rlcosta121/test-app .
docker run -d -p 5000:5000 --name test-app rlcosta121/test-app
docker network connect dockernetwork test-app
docker run -d --name nginx-proxy -p 80:80 --network dockernetwork rlcosta121/nginx-proxy
```
