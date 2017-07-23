from socket import socket, AF_INET, SOCK_DGRAM  
from Queue import Queue
from threading import Thread
from sys import exc_info 
class Server:

	def __init__(self):
		self.sock = socket(AF_INET, SOCK_DGRAM)
		self.sock.bind(("127.0.0.1", 5004)) 
		self.messages = Queue()	
		self.games = Queue()	
		self.thread1 = Thread(target=self.t1, args=("Thread-1", self.messages))
		self.thread2 = Thread(target=self.t2, args=("Thread-2", self.messages))

		self.thread1.start()
		self.thread2.start()

	


	def t1(self, threadname, q):
		while True:
			try:
				data, addr = self.sock.recvfrom(1024)
				q.put((data, addr))
				print("Message:",data,"From",addr)
				if(data == "Leave"):
					return
			except:
				print("Error", exc_info())
				break
	def t2(self, threadname, q):
		while(True):
			try:
				if(q.empty() == False):
					m = q.get()
					if(m[0] == "Join"):
						if(self.games.empty()):
							self.games.put(m[1])
							self.sock.sendto("Joining", m[1])
						else:
							match = self.games.get()
							self.sock.sendto("Joined", match)
							self.sock.sendto("Joined", m[1])
					if(m[0] == "Leave"):
						self.sock.sendto("Leave", m[1])				
						return	
			except:
				print("Error", exc_info())
				break


if __name__ == "__main__":
	s = Server()
