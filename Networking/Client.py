import socket
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
		self.a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.a.bind(("127.0.0.1", 5002))	
		self.thread1 = Thread( target=self.t1, args=("Thread-1", queue) )
		self.thread2 = Thread( target=self.t2, args=("Thread-2", queue) )

		self.thread1.start()
		self.thread2.start()





	def t1(self, threadname, q):
	
    		while True:
			self.data, self.addr = self.a.recvfrom(1024)
			q.put(self.data)
			if(self.data == "Joined"):
				break


	def t2(self, threadname, q):
		
		while(True):
        		try:		
				self.m = str(raw_input("Please Enter a Message: "))	
  			except:
				print("Error,", sys.exc_info())
				break	
			if(self.m in self.commands):		
				self.a.sendto(self.m, ("127.0.0.1", 5004))
			if(q.empty() == False):
				self.m = q.get()	
				if(self.m == "Joining"):	
					print("Joining...")
				if(self.m == "Joined"):
					print("Joined")	
				
				if(self.m == "Leave"):
					return	
			elif(q.emtpy() == True):
				if(self.m == "Leave"):
					return	
			time.sleep(1)
			
		q.put(None) # Poison pill


if __name__ == "__main__":
	c = Client()




