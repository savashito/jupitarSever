from ServerStreamer import ServerStreamer

server = ServerStreamer()

# save the first 100 frames in a file

server.saveFrames(110)


import numpy as np
import cv2

# cap = cv2.VideoCapture('miau2')

# while(cap.isOpened()):
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()