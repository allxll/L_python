from wsgiref.simple_server import make_server

from hellowsgi import application

httpd = make_server('', 8000, application)
print('Serving HTTPPP on porttt 8018080...')
httpd.serve_forever()
