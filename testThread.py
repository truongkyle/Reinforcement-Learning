import threading
import time
from typing import Counter

count = 0
def printTime(namethread):
    global count
    while True:
        time.sleep(5)
        print("%s : %s"%(namethread, str(count)))
threads = []
def timeCounting():
    global count
    while True:
        time.sleep(2)
        count +=1
    
for i in range(2):
    thread = threading.Thread(target= printTime, args = (str(i),))
    thread.start()
    threads.append(thread)
a = threading.Thread(target=timeCounting)
a.start()
