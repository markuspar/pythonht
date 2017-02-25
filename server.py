import socket
import threading
import _thread
from auto import *
import pyDes

class Server(threading.Thread):

	port = None
	host = None


	def __init__(self,port):
		threading.Thread.__init__(self)
		try:
			self.port = int(float(port))
		except:
			self.port = 8080


	def run(self):
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		ss.bind(('', self.port))
		ss.listen(1)

		
		clt,adr = ss.accept()
		msg = clt.recv(1024)
		print(msg.decode("ISO-8859-1"))
		demsg = self.do_decrypt(msg)
		data = demsg.decode("utf-8")
		print(data)
		if (data.strip() == "Draw with paint"):
			bot = Bot('', 'paint')
			bot.start()

		else:
			bot = Bot(data.strip(),'browser')
			bot.start()
		print("Client connected")
		clt.close()

	def do_decrypt(self, req):
		data = req
		k = pyDes.des(b"DESCRYPT", pyDes.CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=pyDes.PAD_PKCS5)
		return k.decrypt(data)
