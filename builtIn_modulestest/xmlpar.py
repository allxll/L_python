from xml.parsers.expat import ParserCreate


class WeatherSaxHandler(object):
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            print (attrs.get('city'))


with open('weatherdata', 'r') as f:
    xml = f.read()



hander = WeatherSaxHandler()
parser = ParserCreate()
parser.StartElementHandler = hander.start_element
parser.Parse(xml)
