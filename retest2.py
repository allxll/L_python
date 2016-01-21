import re
import requests
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'}
old_url = 'http://www.jikexueyuan.com/course/android/?pageNum=2'
t = requests.get(old_url, headers=headers)
with open('datafromjike.txt', 'w') as f:
    f.write(t.text)

