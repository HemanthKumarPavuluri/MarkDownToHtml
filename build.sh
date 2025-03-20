#!/bin/bash

REPO_NAME="MarkDownToHtml"

echo "Building site with base path /$MarkDownToHtml/..."
python3 src/main.py "/$MarkDownToHtml/"

echo "Site successfully built in the docs directory."

