ffplay -rtsp_transport tcp -i rtsp://atwk:ea33ak@192.168.11.50
ffplay -rtsp_transport tcp -i rtsp://admin:password@192.168.11.53
./openRTSP -u admin password rtsp://192.168.11.53
/dev/ttyUSB0
2400
01
ffmpeg -rtsp_transport tcp -i rtsp://atwk:ea33ak@192.168.11.50 -t 10 -c:v copy -f mp4 output.mp4
https://zalinux.ru/?p=5085