# -*- coding: utf-8 -*-
import subprocess as sp
import cv2 as cv
import sys
import time

rtspUrl = 'rtsp://127.0.0.1:8554/live/123'
#camera_path = sys.argv[1]
camera_path = 0
cap = cv.VideoCapture(camera_path, cv.CAP_V4L2)

# Get video information
# fps = int(cap.get(cv.CAP_PROP_FPS))
fps = 15
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# ffmpeg command
command = ['ffmpeg',
        '-y',
        '-f', 'rawvideo',
        '-vcodec','rawvideo',
        '-pix_fmt', 'bgr24',
        #'-s', "{}x{}".format(width, height),
        '-s', "{}x{}".format(640, 480),
        '-r', str(fps),
        '-i', '-',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-tune:v', 'zerolatency',
        '-preset', 'ultrafast',
        #'-f', 'flv',
        '-f', 'rtsp',
        rtspUrl]

# 管道配置
p = sp.Popen(command, stdin=sp.PIPE)

# read webcamera
while(cap.isOpened()):
    ret, frame = cap.read()
    #frame = cv.resize(frame, (width, height))
    time_str = time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
    cv.putText(frame, time_str, (20, 30), cv.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
    if not ret:
        print("Opening camera is failed")
        break

    # process frame
    # your code
    # process frame

    # write to pipe
    p.stdin.write(frame.tostring())