import requests
re = requests.post("https://onepiece.nchu.edu.tw/cofsys/plsql/crseqry_home",
data={'v_career':'U','v_dept':'U56','v_level':'2'})
# 裏面可以放任意的網址
# data這個參數裏面放的是我們提交表單的參數

print(re.text) 
# 這樣就可以看到該網頁的html