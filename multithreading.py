import time
import Threading
import math

def calc_sqrt():
	print("Calculating square roots:")
	n=1
	while (n < 300):
		time.sleep(0.1)
		sqrt = math.sqrt(n)
		print("Sqrt of ", n, ": ", sqrt)
		n+=1

def calc_square():
	print("Calculating square roots:")
	n=1
	while (n < 300):
		time.sleep(0.1)
		square = n*n
		print("Sqrt of ", n, ": ", square)
		n+=1

thread1 = threading.Thread(target=calcsqrt)
thread2 = threading.Thread(target=calcsquare)

thread1.start()
thread2.start()

thread1.join()
thread2.join()