import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
myhead = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'}
te = requests.get(url, headers=myhead)
text = re.findall('<!--(.*?)-->', te.text, re.S)
lines = text[0].split('\n')
with open('equalitydata.txt', 'w') as f:
    f.write(lines)
L = ''
for line in lines:
    print(line)
    for i in range(len(line)):
        pass

