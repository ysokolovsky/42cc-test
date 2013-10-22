from test42cc.contact.models import Request


class RequestMiddleware(object):
    def process_request(self, request):
        req = Request(
            path=request.path,
            method=request.method,
            host=request.get_host(),
            priority=1)
        req.save()
        return None
