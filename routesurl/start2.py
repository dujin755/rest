import os

import eventlet
from eventlet import wsgi
from paste.deploy import loadapp
from paste.deploy import appconfig

config = 'api.ini'


def run_server_public(conf, name='public'):
    app = loadapp('config:%s' % conf, name=name)
    config = appconfig('config:%s' % conf, name=name)
    print config
    socket = eventlet.listen(('0.0.0.0', 8080))
    def _start(app,socket):
        wsgi.server(socket, app)
    started_server = eventlet.spawn(_start, app, socket)
    started_server.wait()


def run_server_admin(conf, name='admin'):
    app = loadapp('config:%s' % conf,name=name)
    socket = eventlet.listen(('0.0.0.0', 8090))
    def _start(app, socket):
        wsgi.server(socket, app)
    started_server = eventlet.spawn(_start, app, socket)
    started_server.wait()

fun = {'run_server_admin': run_server_admin,
       'run_server_public': run_server_public}


def start(config):
    servers = []
    for ser in ['run_server_public', 'run_server_admin']:
        gt = eventlet.spawn(fun[ser], os.path.abspath(config))
        servers.append(gt)
    return servers


def wait(servers):
    for server in servers:
        server.wait()


if __name__ == '__main__':
    wait(start(config))
