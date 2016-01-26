import requests
import re
num='63579'
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
myhead = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'}
for i in range(150):
    te = requests.get(url+num, headers=myhead)
    text = re.search('\d+', te.text)
    print(te.text)
    num = text.group(0)
