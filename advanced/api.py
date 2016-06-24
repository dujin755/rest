import json
import webob.dec
from webob import Response
from webob.exc import HTTPBadRequest


class API(object):

    def create(self, req, body):
        return Response(status=202, body=body, content_type='application/json')

    def index(self, req):
        body = {'method': 'index'}
        return json.dumps(body)

    def show(self, req, id):
        body = {id: 'Call the method show'}
        return Response(body=json.dumps(body), content_type='application/json')

    def update(self, req, id, body):
        return Response(status=202, body=body, content_type='application/json')

    def delete(self, req, id):
        return Response(status=204, content_type='application/json')

    @webob.dec.wsgify
    def __call__(self, req):
        if req.content_type != 'application/json':
            return HTTPBadRequest(message='Only application/json was suppored')
        action_args = req.environ['wsgiorg.routing_args'][1]
        method = getattr(self, action_args['action'])
        action_args.pop('action')
        action_args.pop('controller')
        try:
            resp = method(req, **action_args)
        except TypeError:
            action_args['body'] = req.body
            resp = method(req, **action_args)

        return resp
