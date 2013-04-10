#!/bin/bash/
caMount=$(ls /dev/ | grep -c video0)
if [ "$caMount" == 0 ]; then
	echo "Camera Not Found at video0"
	echo "Searching for Camera at video1"
	caMount=$(ls /dev/ | grep -c video1)
	if [ "$caMount" == 0 ]; then
		echo "Camera Not Found at video1"
		echo "Searching For Other Cameras"
		caMount=$(ls /dev/ | grep -c video)
		if [ "$caMount" == 0 ]; then
			echo "No Cameras Found"
		else
			addCam=$(ls /dev/ | grep -E video)
			echo "Camera(s) found at:"
			echo $addCam
			echo "Which Camera Should Be Used For Streaming?"
			read -e streamCam
			cd /usr/local/src/mjpg-streamer-r63/mjpg-streamer-r63 && ./mjpg_streamer -i './input_uvc.so -d /dev/$streamCam -r 320x240 -f 10' -o './output_http.so -n -c iantbaldwin:besucher -w ./www -p 8080'
		fi
	elif [ "$caMount" == 1 ]; then
	echo "Camera Found at video1" 
	cd /usr/local/src/mjpg-streamer-r63/mjpg-streamer-r63 && ./mjpg_streamer -i './input_uvc.so -d /dev/video0 -r 320x240 -f 10' -o './output_http.so -n -c iantbaldwin:besucher -w ./www -p 8080'	
	fi	
elif [ "$caMount" == 1 ]; then
	echo "Camera Found at video0" 
	cd /usr/local/src/mjpg-streamer-r63/mjpg-streamer-r63 && ./mjpg_streamer -i './input_uvc.so -d /dev/video0 -r 320x240 -f 10' -o './output_http.so -n -c iantbaldwin:besucher -w ./www -p 8080'
fi
#End of File