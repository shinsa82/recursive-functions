#!/bin/bash
docker run -d --rm \
    -p 8888:8888 \
    -v $(pwd):/home/jovyan/work \
    jupyter/tensorflow-notebook
