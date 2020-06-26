import threading 
import time

class myThread(threading.Thread):

    def __init__(self, threadID, name, count):
        threading.Thread.__init__(self)
        self.threadID=threadID
        self.name=name
        self.count=count

    def run(self):
        print("Starting "+ self.name + "\n")
        
          