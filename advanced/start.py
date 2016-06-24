import os
from paste.deploy import loadapp
from paste.deploy import appconfig
from wsgiref.simple_server import make_server

if __name__ == '__main__':
    configfile='config.ini'
    appname='public'
    wsgi_app = loadapp('config:%s' % os.path.abspath(configfile), appname)
    config = appconfig('config:%s' % os.path.abspath(configfile), appname)
    server = make_server(config.get('host', '0.0.0.0'),
                         int(config.get('port', 8080)), wsgi_app)
    server.serve_forever()

