import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self )
        self.h=i
    def run(self):
        time.sleep(5)
        print("value send",self.h)
thread1=mythread(1)
thread1.start()
thread2=mythread(2)
thread2.start()

import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("No. is ",self.h )
for i in range(10):
    thread1=mythread(i)
    thread1.start()
    time.sleep(1)
print("Active threads are",threading.active_count())

import threading
import time
class mythread(threading.Thread):
    def __init__(self,i):
        threading.Thread.__init__(self)
        self.h=i
    def run(self):
        print("hello i m in run",self.h)
thread1=mythread("from thread 1")
thread1.start()
thread1.join()
thread2=mythread("from thread 2")
thread2.start()
thread2.join()

print("\n good bye")




