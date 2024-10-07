from curses.ascii import HT
from dataclasses import dataclass
from email import header
from wsgiref import headers
from products.models import Product
from datetime import date
import imp
from pyexpat import model
from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict



def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    # return HttpResponse(json_data_str,headers = {'content-Type': 'application/json'})

"""
def api_home(request, *args, **kwargs):
    # serialization :
    # model instance (model_data)
    # turn into Python dict
    # return Json to myclient
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    # serialization 
    return JsonResponse(data)

"""
"""
def api_home(request, *args, **kwargs):
    print(request.GET) # url query params
    print(request.POST)
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

"""
