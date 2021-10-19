import threading
import re
import requests
import os
from bs4 import BeautifulSoup
from tqdm import tqdm

pid = 0
approx_images = 0
download_folder = input('Download folder  : ')

if not os.path.exists('btb/output/' + download_folder):
    os.makedirs('btb/output/' + download_folder)

download_folder = 'btb/output/' + download_folder
site = input('URL              : ')
pages = int(input('Pages            : '))

print('========================================')
approx_images = 42*pages
print('Approx. Images   :', approx_images)



class myThread (threading.Thread):
   def __init__(self, threadID, name, pid):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.pid = pid
   def run(self):
        image_count = 0
        if pages >1:
            response = requests.get(site + '&pid=' + str(self.pid))
        else:
            response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]
        
        for url in tqdm(urls, leave=False):
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))', url)
            if not filename:
                print("Regex didn't match with the url: {}".format(url))
                continue
            with open(os.path.join(download_folder, filename.group(1)), 'wb') as f:
                image_count += 1
                #print('[', image_count , '/' , 42 , ']', filename.group(1))
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)

thread_list = []

for i in range(pages):
    thread_list.append(myThread(1, "Thread-" + str(i), pid))
    pid += 40
    thread_list[i].start()