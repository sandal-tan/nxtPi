#!/bin/bash/

cd /usr/local/src/mjpg-streamer-r63/mjpg-streamer-r63 && ./mjpg_streamer -i './input_uvc.so -d /dev/video1 -r 320x240 -f 10' -o './output_http.so -n -c iantbaldwin:besucher -w ./www -p 8080'
