import requests
import certifi

proxy = {
  'http': '217.195.204.86',
  'https': '160.16.215.141',
}

requests.get('https://gelbooru.com/index.php?page=post&s=list&tags=sort%3Ascore%3Adesc+rating%3Asafe+solo+roboco-san&pid=84',
proxies=proxy)
