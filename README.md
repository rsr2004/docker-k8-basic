


## run the test-app

docker build -t test-app .
docker run -d -p 5000:5000 test-app


## run the nginx-proxy
docker build -t rlcosta121/nginx-proxy
docker run -d --name nginx-proxy -p 80:80 --link test-app rlcosta121/nginx-proxy


## Create a network so that the proxy works

docker network create mynetwork
