import socket


import random
import struct
import cv2
import numpy as np
import time
from ServerStreamer import ServerStreamer


streamkey = "live_112595746_ll4Ij7ggf17kutQzcVngpVaNtJtDH3"
cv2.namedWindow("preview")
# vc = cv2.VideoCapture(0)
from twitchstream.outputvideo import TwitchBufferedOutputStream

# if vc.isOpened(): 
	# rval, frame = vc.read()
server = ServerStreamer()
with TwitchBufferedOutputStream(
		twitch_stream_key=streamkey,
		# width=640,
		# height=480,
		width=960,
		height=720,
		fps=30.,
		enable_audio=True,
		verbose=False) as videostream:
	while True:
		server.accept()
		c = server.getBytesImage()
		cv2.imshow("preview", c)
		key = cv2.waitKey(20)
		# print c
		if videostream.get_video_frame_buffer_state() < 30:
			videostream.send_video_frame(c)
		else:
			time.sleep(1)
		'''
		rval, frame = vc.read()
		floatlist = frame.ravel()
		floatlist.shape = (720, 1280, 3)
		floatlist = floatlist/255.0
		cv2.imshow("preview", floatlist)
		key = cv2.waitKey(20)
		print "Sending frame "+str(floatlist.shape)
		if videostream.get_video_frame_buffer_state() < 30:
			videostream.send_video_frame(floatlist)
		else:
			time.sleep(1)
			#print "Sent frame "+str(frame.shape)
		'''

