#!/bin/bash

# Variables
IMAGE_NAME="show-host-details"
CONTAINER_NAME="shd-container"
DOCKERFILE="Dockerfile"
WORKDIR=$(pwd)

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

if [ $? -ne 0 ]; then
    echo "Error: Docker build failed."
    exit 1
fi

echo "Docker image built successfully."

# Run the Docker container
echo "Running Docker container..."
docker run -it --name $CONTAINER_NAME --rm $IMAGE_NAME

if [ $? -ne 0 ]; then
    echo "Error: Failed to run the container."
    exit 1
fi

echo "Docker container has stopped."
