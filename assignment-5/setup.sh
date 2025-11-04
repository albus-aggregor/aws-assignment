#!/bin/bash
set -e

echo "Setting up environment..."

# Check Docker
if ! command -v docker &> /dev/null
then
    echo "Docker not found. Please install Docker."
    exit 1
fi

# Check Docker Compose
if ! command -v docker compose &> /dev/null
then
    echo "Docker Compose not found. Please install Docker Compose."
    exit 1
fi

# Build and start containers
echo "Building and starting services..."
docker compose up -d --build

# Wait for health checks
echo "Waiting for services to become healthy..."
sleep 20
docker compose ps

# Logs
echo "Showing logs..."
docker compose logs -f
