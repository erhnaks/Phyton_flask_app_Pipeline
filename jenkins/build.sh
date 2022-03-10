#!/bin/bash

echo "Build Stage"

docker swarm init

#build Docker s

docker stack deploy --compose-file docker-compose.yaml pizzaapp