import logs
from routes import Mapper
from webob import request

LOG = logs.getLogger(__name__)

class Server(object):

    def create(self, body):
        return {'method': 'create'}

    def index(self):
        return {'method': 'index'}

    def show(self, id):
        return {'method': 'get'}

    def delete(self, id):
        return {'method': 'delete'}

    def update(self, id, body):
        return {'method': 'update'}


class Public(object):

    def __init__(self, conf):
        self.conf = conf
        self.mapper = Mapper()
        self.mapper.resource('server', 'servers', controller=Server())

    def __call__(self, env, start_response):
        kwargs = self.mapper.match(environ=env)
        req = request.Request(env)
        LOG.error(kwargs)
        LOG.error(req)
        LOG.error(req.body)
        start_response('200 OK', [('Content-Type', 'application/json')])
        return ['Hello Public']


class Admin(object):

    def __init__(self, conf):
        self.conf = conf

    def __call__(self, env, start_response):
        start_response('200 OK', [('Content-Type', 'application/json')])
        return ['Hello Admin']


def public_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Public(conf)


def admin_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Admin(conf)
