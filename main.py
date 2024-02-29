import requests
from bs4 import BeautifulSoup

r = requests.get("https://netinfo.takming.edu.tw/tip/home_new.php") #將此頁面的HTML GET下來
print(r.text) #印出HTML