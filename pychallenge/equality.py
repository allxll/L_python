import requests
import re
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
myhead = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'}
te = requests.get(url, headers=myhead)
text = re.findall('<!--(.*?)-->', te.text, re.S)
lines = text[0].split('\n')
L = []
for row, line in enumerate(lines):
    for i, ch in enumerate(line):
        if i < 3 or i > len(line) - 4: continue
        s = line[i-3:i]+line[i+1:i+4]
        if s.isupper() and ch.islower():
            if i == 3 or i == len(line) - 4:
                L.append(ch)
                print(ch, row, i, sep="------")
            elif (line[i-4]+line[i+4]).islower():
                L.append(ch)
                print(ch, (line[i-4]+line[i+4]), row, i, sep="------")
print(L)
