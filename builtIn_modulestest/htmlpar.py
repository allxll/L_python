from html.parser import HTMLParser
import requests
url = 'https://www.python.org/events/python-events/'
headers = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.106 Chrome/47.0.2526.106 Safari/537.36'}
tx = requests.get(url, headers=headers)
print(tx.text)


class MyHTMLParser(HTMLParser):

    _in_title = False
    _in_title_ref = False
    _in_time = False
    _in_location = False

    def handle_starttag(self, tag, attrs):
        if ('class', 'event-title') in attrs:
            self._in_title = True
        if tag == 'a' and self._in_title:
            self._in_title_ref = True
        if tag == 'time':
            self._in_time = True

    def handle_endtag(self, tag):
        if self._in_title and tag == 'h3':
            self._in_title = False
        if self._in_title and tag == 'a':
            self._in_title_ref = False
        if self._in_time and tag == 'time':
            print()
            self._in_time = False

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_data(self, data):
        if self._in_time:
            print(data.strip(), end='---')
        if self._in_title_ref:
            print(data)



#parser = MyHTMLParser()
#parser.feed(tx.text)
