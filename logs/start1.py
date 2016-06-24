import os
from paste.deploy import loadapp
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    configfile='api.ini'
    appname='public'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)
    server = make_server('0.0.0.0', 8080, wsgi_app)
    server.serve_forever()
