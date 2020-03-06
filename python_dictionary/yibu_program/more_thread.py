#多线程
from threading import Thread
import time
import schedule

def job1():
	print('this is job1')
	time.sleep(2)
	print('job1 is end')

def job2():
	print('this is job2')
	time.sleep(2)
	print('job2 is end')

def job1_task():
	Thread(target=job1).start()

def job2_task():
	Thread(target=job2).start()

def run():
	schedule.every(5).seconds.do(job1_task)
	schedule.every(5).seconds.do(job2_task)

run()

while True:
	schedule.run_pending()
	time.sleep(1)


