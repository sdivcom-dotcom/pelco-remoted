ffplay -rtsp_transport tcp -i rtsp://atwk:ea33ak@192.168.11.50
/dev/ttyUSB1
2400
01
ffmpeg -rtsp_transport tcp -i rtsp://atwk:ea33ak@192.168.11.50 -t 10 -c:v copy -f mp4 output.mp4
https://zalinux.ru/?p=5085