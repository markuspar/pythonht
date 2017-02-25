import sys
import _thread
from auto import *
from server import *
from client import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QMainWindow,QWidget, QPushButton, 
	 QApplication, QLabel, QLineEdit, QComboBox)
from PyQt5.QtGui import QFont


class Window(QMainWindow):

	portEdit = None
	addrEdit = None
	siteEdit = None
	openButton = None
	paintButton = None
	listenButton = None
	connectButton = None
	requests = None

	currentRequest = "Open URL"

	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):

		label = QLabel("Local",self)
		font = QFont("Times", 15, QFont.Bold)
		label.setFont(font)

		self.openButton = QPushButton("Open in browser",self)
		self.openButton.setObjectName("openBrows")

		siteLabel = QLabel('Enter url',self)
		portLabel = QLabel("Port number",self)
		self.siteEdit = QLineEdit(self)

		self.paintButton = QPushButton("Draw with paint",self)
		self.paintButton.setObjectName("paintBtn")

		self.openButton.clicked.connect(self.buttonClicked)
		self.paintButton.clicked.connect(self.paintButtonClicked)

		label2 = QLabel("Remote", self)
		label2.setFont(font)

		self.listenButton = QPushButton("Receive request", self)
		self.listenButton.clicked.connect(self.serverRun)
		self.portEdit = QLineEdit(self)

		self.connectButton = QPushButton("Send request",self)
		self.connectButton.clicked.connect(self.sendRequest)

		self.addEdit = QLineEdit(self)
		addrLabel = QLabel("Remote address", self)

		self.requests = QComboBox(self)
		self.requests.addItem("Open URL")
		self.requests.addItem("Draw with paint")
		self.requests.currentIndexChanged.connect(self.selectionChanged)

		label.move(100, 25)
		siteLabel.move(50,50)
		self.siteEdit.move(50,75)
		self.openButton.move(200,75)
		self.paintButton.move(200,125)
		self.portEdit.move(50, 250)
		self.listenButton.move(200,250)
		portLabel.move(50,225)
		self.connectButton.move(200,325)
		self.addEdit.move(50,325)
		addrLabel.move(50,300)
		self.requests.move(50, 375)
		label2.move(100, 200)

		self.statusBar()

		self.setGeometry(300, 300, 350, 500)
		self.setWindowTitle('HelperBot')
		self.setFixedSize(self.size())
		self.show()

	def buttonClicked(self):
		try:
			
			self.disableActions()
			b = Bot(self.siteEdit.text(), 'browser')
			_thread.start_new_thread(self.operationRunning, (b,))
			self.statusBar().showMessage("Processing request...")

				
		except:
			print("Thread failure")


	def paintButtonClicked(self):
		try:

			self.disableActions()
			b = Bot(self.siteEdit.text(), 'paint')
			_thread.start_new_thread(self.operationRunning, (b,))
			self.statusBar().showMessage("Processing request...")
		except:
			print("Thread failure")

	def operationRunning(self,b):
		b.start()
		running = 1
		while (running == 1):
			if not b.isAlive():
				running = 0
				self.statusBar().showMessage("Processing completed...")
				self.enableActions()
			else:
				var = "var"

	def serverRun(self):
		try:
			self.disableActions()
			s = Server(self.portEdit.text())
			_thread.start_new_thread(self.operationRunning, (s,))

		except:

			print("Server error")

	def sendRequest(self):
		try:
			self.disableActions()
			if self.currentRequest == "Draw with paint":
				c = Client(self.addEdit.text(),self.portEdit.text(), self.currentRequest)
			else:
				c = Client(self.addEdit.text(),self.portEdit.text(), self.siteEdit.text())
			_thread.start_new_thread(self.operationRunning, (c,))
		except:
			print("Connection failed")

	def selectionChanged(self):
		self.currentRequest = self.requests.currentText()
		print(self.currentRequest)

	def disableActions(self):

		self.openButton.setEnabled(False)
		self.paintButton.setEnabled(False)
		self.listenButton.setEnabled(False)
		self.connectButton.setEnabled(False)
		self.requests.setEnabled(False)
		self.siteEdit.setEnabled(False)
		self.addEdit.setEnabled(False)
		self.portEdit.setEnabled(False)


	def enableActions(self):

		self.openButton.setEnabled(True)
		self.paintButton.setEnabled(True)
		self.listenButton.setEnabled(True)
		self.connectButton.setEnabled(True)
		self.requests.setEnabled(True)
		self.siteEdit.setEnabled(True)
		self.addEdit.setEnabled(True)
		self.portEdit.setEnabled(True)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	win = Window()
	sys.exit(app.exec_())
