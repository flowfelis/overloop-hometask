import json
from django.http.response import HttpResponse


def json_response(data=None, status=200):
    # https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/
    if data is None:
        data = {}
    return HttpResponse(
        content=json.dumps(data), status=status, content_type="application/json"
    )
