#!/bin/bash

xhost +local:
docker run \
     	-it \
        --rm \
	--user root \
        --env="DISPLAY" \
        --env="QT_X11_NO_MITSHM=1" \
        --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
        --name yollov8_container \
        --ipc=host \
	--net=host \
        --gpus all  \
	--volume="$PWD:/root/workspace" \
	--privileged \
        --ulimit memlock=-1 \
	--ulimit stack=67108864 \
	alexandreacff/yollov8-ros-foxy:apha	
