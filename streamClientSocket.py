import socket

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096
# videofile = "videos/royalty-free_footage_wien_18_640x360.mp4"

# bytes = open(videofile).read()
import random
import struct
import cv2
import numpy as np
import time

# random.random()
streamkey = "live_112595746_ll4Ij7ggf17kutQzcVngpVaNtJtDH3"
# floatlist = [i for i in range(10**5)]
cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)
from twitchstream.outputvideo import TwitchBufferedOutputStream

if vc.isOpened(): # try to get the first frame
	rval, frame = vc.read()

with TwitchBufferedOutputStream(
		twitch_stream_key=streamkey,
		# width=640,
		# height=480,
		width=1280,
		height=720,
		fps=30.,
		enable_audio=True,
		verbose=False) as videostream:
	while rval:
		rval, frame = vc.read()
		
		# print (frame.shape)
		floatlist = frame.ravel()
		# print floatlist.dtype
		# bytes = struct.pack('%sf' % len(floatlist), * floatlist)
		# msg = bytes
		# nFloats =  len(msg)/4
		# floatlist = struct.unpack('%sf'% nFloats,msg)
		# image = np.asarray(floatlist)
		floatlist.shape = (720, 1280, 3)
		# floatlist = floatlist[0:480,0:640,:]
		# print floatlist.shape
		# floatlist = cv2.cvtColor(floatlist,cv2.COLOR_BGRA2YUV_I420)

		floatlist = floatlist/255.0
		rgb = [floatlist[:,:,0],floatlist[:,:,1],floatlist[:,:,2]]
		# print 
		cv2.imshow("preview", rgb)
		key = cv2.waitKey(20)
		# floatlist[:,:,0], floatlist[:,:,1], floatlist[:,:,2]=  floatlist[:,:,2],floatlist[:,:,1], floatlist[:,:,0]

		
		# connect to server

		'''
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect(ADDR)

		client.send(floatlist)

		client.close()
		'''

		print "Sending frame "+str(rgb.shape)
		# send to twitch
		

		if videostream.get_video_frame_buffer_state() < 30:
			videostream.send_video_frame(floatlist)
		else:
			time.sleep(1)
			#print "Sent frame "+str(frame.shape)


