import threading
import re
import requests
import os
from bs4 import BeautifulSoup

from tqdm import tqdm
# from tqdm.auto import tqdm  # notebook compatible
import time

class myThread (threading.Thread):
   def __init__(self, threadID, name, pid):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.pid = pid
   def run(self):
        for i in tqdm(range(42)):
            time.sleep(0.3)

thread_list = []

for i in range(3):
    thread_list.append(myThread(1, "Thread-" + str(i), 42))
    thread_list[i].start()