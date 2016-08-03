import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup
json_arr = []

def dump(fileName):
	with open(fileName, 'w', encoding='UTF-8') as f:
		json.dump(json_arr, f)

def parsePage(url):
	res = requests.get(url)
	soup = BeautifulSoup(res.text)

	table = soup.select('body tr td table')[2]
	print(table)
	# for i in soup.select('ul.deal16 li.box-shadow2px'):
	# 	product = i.select('h3.proname_3')[0].text
	# 	restaurant = i.select('h2.ref_name_2')[0].text	
	# 	imghref = i.select('img')[0]['src']

	# 	tmp={}
	# 	# dict這個型態的值是可以改變的 
	# 	# 所以python不會自動幫你建一個新的物件而是用指標（reference）的方式連結到同一個變數
	# 	tmp['product'] = product
	# 	tmp['restaurant'] = restaurant
	# 	json_arr.append(tmp)

	# dump('demo.json')

parsePage('http://www.ibon.com.tw/event/4x6_page/print.html')