from ServerStreamer import ServerStreamer

#server = ServerStreamer()

# save the first 100 frames in a file

#server.saveFrames(110)

#exit()
import numpy as np
import cv2
cv2.namedWindow("frame")
cap = cv2.VideoCapture('miauTNoLimit.h264')
print cap.isOpened()
while(cap.isOpened()):
	ret, frame = cap.read()
	print frame.shape
	#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
# cv2.destroyAllWindows()
