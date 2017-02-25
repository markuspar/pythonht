import socket
import _thread
import threading
import pyDes


class Client(threading.Thread):

	addr = None
	port = None
	requ = None
	s = None

	def __init__(self, addr, port, requ):
		threading.Thread.__init__(self)
		if (addr is not "" and port is not 0):
			self.addr = str(addr).strip()
			self.port = int(float(port))
			self.requ = str(requ)
		else:

			self.requ = str(requ)

		
			self.addr = "127.0.0.1"
			self.port = 8080

	def run(self):

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((self.addr, self.port))
		if(self.requ is not None):
			msg = self.do_encrypt(self.requ)
			print(msg)
			self.s.send(msg)
		self.s.close()

	def do_encrypt(self, req):
		data = str.encode(req)
		k = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
		return k.encrypt(data)
		