from dataclasses import dataclass
from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    print(request.GET) # url query params
    body = request.body # byte sting of data
    data = {}
    try:
        data = json.loads(body) # string of json data -> Python dict
    except:
        pass
    print(data)
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)