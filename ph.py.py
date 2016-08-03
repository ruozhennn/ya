import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup

def savePict(url, restaurant):
    img = requests.get(url,stream=True)
    with open(restaurant+'.jpg', 'wb') as f:
        shutil.copyfileobj(img.raw, f)
savePict("http://i2.disp.cc/imgur7/146Qf.jpg", "test")