import threading
import re
import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

pid = 0
approx_images = 0
download_folder = input('Download folder  : ')
card_id_list = []
current_card = 0




if not os.path.exists('kb/output/' + download_folder):
    os.makedirs('kb/output/' + download_folder)

download_folder = 'kb/output/' + download_folder
site = "https://lostone.kirara.ca/card/card_"
card_id_list = input('Pages            : ').split(',')

thread_job_list_a = card_id_list[:len(card_id_list)//2]
thread_job_list_b = card_id_list[len(card_id_list)//2:]

class myThread (threading.Thread):
    def __init__(self, threadID, name, job):
        global current_card
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.job = job
    def run(self):
        for id in tqdm(self.job):
            filename = str(id) + ".png"
            with open(os.path.join(download_folder, filename), 'wb') as f:
                url = site + str(id) + '.png'
                response = requests.get(url)
                f.write(response.content)


thread_list = []

thread_list.append(myThread(1, "Thread-1", thread_job_list_a))
thread_list.append(myThread(2, "Thread-2", thread_job_list_b))
thread_list[0].start()
thread_list[1].start()