# Volume

[이미지](/DevOps/Docker/Image)로 컨테이너를 실해하면 읽기 전용이 되어 변경사항은 컨테이너에만 저장된다.  
문제 예방을 위해, 데이터를 영속적(Persistent)으로 저장하고자 볼륨을 사용한다.

### 호스트 볼륨 공유
- `-v` 옵션을 통해서 볼륨을 지정할 수 있다. 
- `-p` 옵션과 같이 호스트:컨테이너 형식으로 작성한다.

> 디렉토리가 존재하지 않아도, 도커가 자동으로 생성해준다.  
> 이미 해당 경로가 존재한다면, 호스트의 파일들을 컨테이너에 **Mount** 시켜준다.

```shell
docker pull ubuntu:latest
```

```shell
docker run -it -d \
--name ubuntu1 \
-v /home/for_volume:/home/for_volume \
ubuntu
```
![docker_volume_1](/_images/docker_volume_1.png)
### 볼륨 컨테이너
```shell
docker run -it -d --name ubuntu2 --volumes-from ubuntu1 ubuntu
```
- 볼륨을 공유하고 있는 컨테이너를 통해서 간접적으로 볼륨을 사용할 수가 있다.
- 간접적으로 사용하더라도 변경 사항은 호스트에 적용된다.

![docker_volume_2](/_images/docker_volume_2.png)

### 도커 볼륨
- 도커 엔진에 의해 관리되는 볼륨으로, 어디에 저장되는지 신경쓰지 않아도 된다.
- `-v /conatiner_path`로 사용할 경우, 16진수의 무작위 이름을 가진 볼륨이 생성된다.
- 플러그인 드라이버를 통하여 여러 종류의 스토리지를 설정할 수 있다.

- 기본적으로 제공되는 드라이버는 `local`이다.  
- 기본적으로는 `/var/lib/docker/volumes` 아래에 저장된다.

> [Window와 MacOS의 경우 도커가 가상환경에서 실행되기에, 실제로는 다른 환경에 저장되어 있다.](https://amazelimi.tistory.com/entry/Docker-Volume-%EC%82%AC%EC%9A%A9%EC%8B%9C-mac-%EC%97%90-varlibdocker-%EA%B2%BD%EB%A1%9C%EA%B0%80-%EC%97%86%EB%8A%94-%EC%9D%B4%EC%9C%A0-LIM)

```shell
# Volume 생성 
$ docker volume create --name myvolume

# Volume 리스트
$ docker volume ls

# Docker run에 사용
$ docker run -it -v myvolume:/root/ ubuntu

# Volume 상세 정보 조회
$ docker inspect volume myvolume
[
    {
        "CreatedAt": "2024-03-20T18:35:48+09:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/myvolume/_data",
        "Name": "myvolume",
        "Options": null,
        "Scope": "local"
    }
]
```
