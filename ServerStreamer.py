import socket
import numpy as np
class ServerStreamer:
	def __init__(self):
		serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		HOST = socket.gethostname() # '' # 54.153.114.110
		PORT = 80
		ADDR = (HOST,PORT)
		self.BUFSIZE = 4096
		
		serv.bind(ADDR)
		self.port = PORT
		serv.listen(5)
		self.serv = serv
		

	def accept(self):
		#print 'Listening for connections on port ',self.port
		self.conn, self.addr = self.serv.accept()
		#print 'client connected ... ', self.addr
	def getRawBytes(self):
		b = bytearray()
		while True:
			chunk = self.conn.recv(self.BUFSIZE)
			# print chunk
			if not chunk: break
			# msgparts.append(chunk)
			b.extend(chunk)
		return b
	def saveFrames(self,nFrames):
		fOut = open("miauTNoLimit.h264", 'wb')
		for i in range(nFrames):
			self.accept()
			bytes = self.getRawBytes()
			print "Recieved %d bytes"%len(bytes)
			if len(bytes)<3:
				continue
			fOut.write(bytes)
			print "%d %d %d %d "%(bytes[0],bytes[1],bytes[2],bytes[3])
			# fOut.write(b'\0\0\0\1' + bytes)

	def getBytesImage(self):

		c = np.uint8(self.getRawBytes())
		dim = None
		if( len(c) ==720*960*4):
			dim = 960
			c = c.reshape(720,dim,4)
		elif( len(c) ==720*1280*4):
			dim = 1280
			c = c.reshape(720,dim,4)
		c = c/255.0
		rgb = np.delete(c,3,2)# np.array([c[:,:,0],c[:,:,1],c[:,:,2]]).reshape(720,dim,3)

		
		print rgb.shape
		self.conn.close()
		print 'client disconnected'
		# print c
		# print c[:,:,0]
		# print c[:,:,3]
		# print c[:,:,0].shape
		# c[:,:,1], c[:,:,2], c[:,:,0]=  c[:,:,2],c[:,:,0], c[:,:,1]
		return rgb
