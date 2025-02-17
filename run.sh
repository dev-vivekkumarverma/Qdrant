#!/bin/bash

echo "Starting Docker containers..."
docker-compose up -d

echo "Waiting for services to start..."
sleep 10  # Wait for PostgreSQL and Qdrant to be fully ready

# echo "Creating a virtual environment..."
# python3 -m venv venv

# echo "Activating the virtual environment..."
# source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Populating Qdrant with vector data..."
python vector_store.py

echo "Starting the search application..."
echo "type exit in query to exit"
python main.py


echo "stopping the containers.."
docker-compose stop

# echo "removing the containers.."
# docker-compose down

# echo "removing all stored data.."

# docker-compose down -v
