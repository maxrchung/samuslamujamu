import socket
from Queue import Queue


class Server:

	def __init__(self):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(("127.0.0.1", 5004)) 
		self.games = Queue()	
		while(True):	
			self.data, self.addr = self.sock.recvfrom(1024)
			print("Message:", self.data, "From:", self.addr)	
			if(self.data == "Leave"):
				break
			if(self.data == "Join"):
				if(self.games.empty()):
					self.games.put(self.addr)
					self.sock.sendto("Joining", self.addr)
				else:
					self.match = self.games.get()
					self.sock.sendto("Joined", self.match)
					self.sock.sendto("Joined", self.addr)	


if __name__ == "__main__":
	s = Server()
