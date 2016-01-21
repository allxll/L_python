import requests
url1 = 'http://www.crowdfunder.com/browse/deals'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36'}
html = requests.get(' headers = headers)
print(html.text)
