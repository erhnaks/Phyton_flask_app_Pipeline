#!/bin/bash

echo "Build Stage"



#build Docker images

docker stack deploy --compose-file docker-compose.yaml pizzaapp