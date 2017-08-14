#!/bin/bash
while true; do
  DATE=$(date +"%Y%m%d-%H%M%s")
  fswebcam -r 1280x720  /home/pi/Desktop/Ornekler/images/$DATE.JPEG
  sleep 5
done
