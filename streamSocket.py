from ServerStreamer import ServerStreamer
import struct
import cv2
import numpy as np



print 'listening ...'
cv2.namedWindow("preview")

def YUV_stream2RGB_frame(stream):
	w=1280
	h=720
	size=w*h
	print stream
	# stream=np.fromstring(data,np.uint8) #convert data form string to numpy array

	#Y bytes  will start form 0 and end in size-1 
	y=stream[0:size].reshape(h,w) # create the y channel same size as the image

	#U bytes will start from size and end at size+size/4 as its size = framesize/4 

	u=stream[size:(size+(size/4))].reshape((h/2),(w/2))# create the u channel its size=framesize/4

	#up-sample the u channel to be the same size as the y channel and frame using pyrUp func in opencv2
	u_upsize=cv2.pyrUp(u)

	#do the same for v channel 
	v=stream[(size+(size/4)):].reshape((h/2),(w/2))
	v_upsize=cv2.pyrUp(v)
	#create the 3-channel frame using cv2.merge func watch for the order
	yuv=cv2.merge((y,u_upsize,v_upsize))
	# print yuv.shape
	print yuv
	#Convert TO RGB format

	# rgb=cv2.cvtColor(yuv,cv2.COLOR_YUV2BGR)
	rgb=cv2.cvtColor(yuv,cv2.cv.CV_YCrCb2RGB)

	#show frame
	cv2.imshow("preview",rgb)
	cv2.waitKey(5)

server = ServerStreamer()

while True:
	server.accept()
	c = server.getBytesImage()
	# myfile = open('testfile.mov', 'w')
	# msgparts = []
	
	# msg = b"".join(msgparts) 
	
	# b.extend(msg)
	# nFloats =  len(msg)/4
	#floatlist = struct.unpack('%sf'% nFloats,msg)
	# c = np.uint8(b)


	# c[:,:,0], c[:,:,0], c[:,:,2],c[:,:,2] = c[:,:,2], c[:,:,0]
	print c.shape
	# rgb=cv2.cvtColor(c,cv2.cv.COLOR_RGBA2BGR)

	# print rgb.shape

	# c = c.reshape(720/2,1280,3)
	# print len(c)
	# print c
	#YUV_stream2RGB_frame(c)
	#print c
	# c = c.reshape(720/2,1280,3)
	# COLOR_YUV420p2BGR
	# d = cv2.cvtColor(c,cv2.COLOR_YUV4202BGR)
	# print d.shape

	cv2.imshow("preview", c)
	key = cv2.waitKey(20)

	'''
	print len(b)
	b = np.uint8(b).reshape(-1,1)
	print b
	bytes = (b & np.array([0xF,0xF0],dtype=np.uint8)) >> np.array([0, 4], dtype=np.uint8)
	print bytes
	bytes = (bytes+1)*16-1
	print bytes

	bytes.shape = (720, 1280, 3)
	print bytes.shape
	c = bytes
	# c = cv2.cvtColor(bytes,cv2.COLOR_YUV2BGR)

	print c.shape
	cv2.imshow("preview", c)
	'''
	'''
	floatlist = np.uint8(b)
	# COLOR_YUV2BGR_I420
	floatlist = cv2.cvtColor(floatlist,cv2.COLOR_YUV2BGR_I420)
	print floatlist.shape
	
	if( len(floatlist) == 720 * 1280 *3):
		floatlist.shape = (720, 1280, 3)
	elif ( len(floatlist) == 720 * 1280 *4):
		floatlist.shape = (720, 1280, 4)
	else:
		print "error "+str(floatlist.shape)
		continue 1382400
	# print 720 * 1280 *3
	
	
	# print floatlist [700]
	cv2.imshow("preview", floatlist)
	key = cv2.waitKey(20)
	if key == 27: # exit on ESC
		break
	# '''
	

cv2.destroyWindow("preview")



def YUV2BGR_I420(floatlist):
	if( len(floatlist) == 720 * 1280 *3/2):
		floatlist.shape = (720, 1280, 2)
	elif ( len(floatlist) == 720 * 1280 *4):
		floatlist.shape = (720, 1280, 4)
	else:
		print "error "+str(floatlist.shape)