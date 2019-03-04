#!/bin/bash

if ! [ -f datasets/bouncing_ball/images.zip ]; then
    echo "Downloading"
    curl -L -o datasets/bouncing_ball/images.zip 'https://drive.google.com/uc?authuser=0&id=1nVROaX5sO3sxpbCEAn-ehpG5qzDAFj9K&export=download'
    unzip datasets/bouncing_ball/images.zip -d datasets/bouncing_ball
else
    echo "File exists"
fi
