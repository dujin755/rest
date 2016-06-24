import routes
import routes.middleware
import webob.dec
from webob.exc import HTTPNotFound

from api import API

class Public(object):

    def __init__(self, conf):
        self.conf = conf
        self.mapper = routes.Mapper()
        self.mapper.resource('server', 'servers', controller=API())
        self._router = routes.middleware.RoutesMiddleware(self._dispatch,
                                                          self.mapper)

    @webob.dec.wsgify
    def __call__(self, req):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            return HTTPNotFound()
        app = match['controller']
        return app


def public_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    return Public(conf)
