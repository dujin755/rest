class Public(object):

    def __init__(self, conf):
        self.conf = conf

    def __call__(self, env, start_response):
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
