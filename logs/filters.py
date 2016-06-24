class Auth(object):

    def __init__(self, conf, app):
        self.conf = conf
        self.app = app

    def __call__(self, env, start_response):
        return self.app(env, start_response)


def filter_factory(global_conf, **local_conf):
    conf = global_conf.copy()
    conf.update(local_conf)
    def filter_filte(app):
        return Auth(conf, app)
    return filter_filte
