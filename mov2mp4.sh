#!/bin/bash

OLD_FILENAME=$1
NEW_FILENAME=$(uuidgen)
echo $OLD_FILENAME.mov
ffmpeg -i "$OLD_FILENAME.mov" $NEW_FILENAME.mp4 && rm "$OLD_FILENAME.mov"

