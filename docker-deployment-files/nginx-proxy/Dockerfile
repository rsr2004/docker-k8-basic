# Dockerfile.nginx
FROM nginx:alpine

COPY server.crt /etc/nginx/server.crt
COPY server.key /etc/nginx/server.key

COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 443 80
