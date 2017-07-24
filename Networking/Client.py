from threading import Thread
from Queue import Queue
import time
import socket
import sys

class Client:
	def __init__(self):
		self.inGame = False
		queue = Queue()
		self.commands = ['Join', 'Leave']

		self.sock.bind(("127.0.0.1", 5002))	
		self.thread1 = Thread( target=self.t1, args=("Thread-1", queue) )
		self.thread2 = Thread( target=self.t2, args=("Thread-2", queue) )

		self.thread2.start()
		self.thread1.start()

	def t1(self, threadname, q):
	
    		while True:
			#Receiving Messages from the Server
			data, addr = self.sock.recvfrom(1024)
			q.put(data)
			if(data == "Leave"):
				return	


	def t2(self, threadname, q):
		
		while(True):
        		try:	
				#Sending Messages to the Server	
				output = str(raw_input("Please Enter a Message: "))	
				if(output in self.commands):		
					self.sock.sendto(output, ("127.0.0.1", 5004))
				
				time.sleep(1)

				#Handling Messages from Server
				if(q.empty() == False):
					message = q.get()	
					if(message == "Joining"):	
						print("Joining...")
					if(message == "Joined"):
						print("Joined")	
					if(message == "Leave"):
						print("Leave")	
						return	
  			except:
				print("Error,", sys.exc_info())
				break	




if __name__ == "__main__":
	c = Client()




