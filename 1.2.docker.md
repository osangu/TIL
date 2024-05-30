# Docker

## Image
### Layer

## Container
### Runtime




# Registry
```shell
docker run -d --restart=always -v registry-vol:/var/lib/registry -v registry-htpasswd-vol:/auth -e REGISTRY_AUTH=htpasswd -e REGISTRY_AUTH_HTPASSWD_REALM="Username and Password required" -e REGISTRY_STORAGE_DELETE_ENABLED=true -e REGISTRY_AUTH_HTPASSWD_PATH=/auth/htpasswd --name image-registry --network=nginx-bridge registry
```


### image-registry-viewer
```shell
docker run -it -d --name image-registry-viewer -e DOCKER_REGISTRY_URL=http://image-registry:5000 -e NO_SSL_VERIFICATION=false -e TOKEN_AUTH_USER=admin -e TOKEN_AUTH_PASSWORD=nimda12# -e SECRET_KEY_BASE=aab75866e477daabcdfc04d3aa50f08da90a0450dfbafd96537f48f1a3fcbe7a9c3ddbde4be3389e1c1ada13b0ca313611f97ab6e5a10452ebc5c0a11ea5b9b5 --restart=always  --network=nginx-bridge klausmeyer/docker-registry-browser 
```


### image-registry-ui
```shell
docker run -it -d -e DELETE_IMAGES=true -e NGINX_PROXY_PASS_URL=http://image-registry:5000 -e SHOW_CATALOG_NB_TAGS=true -e REGISTRY_SECURED=true --name image-registry-ui --network nginx-bridge joxit/docker-registry-ui:main
```
