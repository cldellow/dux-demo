from datasette import hookimpl
from urllib.parse import urlparse, parse_qs

@hookimpl
def actor_from_request(request):
    url = urlparse(request.url)
    qs = parse_qs(url.query)

    if '_whoami' in qs and len(qs['_whoami']) == 1:
        return {'id': qs['_whoami'][0]}
