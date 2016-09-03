'''prints fibonacci series upto 50 values.
This module provides class fib
'''
class Fib(object):
	'''Class Fib
  	Methods::
  	 fibo() , hello() 
	'''
	def __init__(self,n):
		print "class created"
		self.n=n
	def fibo(self,n):
		'''prints fibonacci series.
		'''
		a,b=0,1
		for x in range(self.n):
			c=a+b		
			print c
			a=b
			b=c
	def hello(self):
		'''prints statement'''
		print "hello world"
		
	def fun(self):
		i=self.n/2
		j=1
	
		for x in range(self.n/2+1):
			if x<=self.n/2:
				for y in range(self.n/2-i+1):
					print y,
					
			i=i-1
			print ' '
		for x in range(self.n/2):
			for z in range(self.n/2-j+1):
				print z,
			print ''
			j=j+1
	def print_all(self):
		self.hello()
		self.fun(self.n)
		self.fibo()
print __name__
if __name__=='__main__':
	f=Fib(10)
	f.fibo()
	f.hello()	
		

