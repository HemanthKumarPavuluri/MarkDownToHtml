#!/bin/bash

echo "Deleting docs directory..."
rm -rf docs  # Delete old build to avoid conflicts

echo "Building site..."
python3 src/main.py "/"

echo "Starting local development server..."
cd docs && python3 -m http.server 8888

