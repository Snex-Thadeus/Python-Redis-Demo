from async_timeout import timeout
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from .models import *

# Create your views here.
def home(request):
    payload = []
    db = None   
    if cache.get('fruits'):
        payload = cache.get('fruits')
        db = 'redis'
        #print(cache.ttl("fruits"))
    else:
        objs = Fruits.objects.all()
        
        for obj in objs:
            payload.append(obj.fruit_name)
        db = 'sqlite'

        cache.set('fruits', payload, timeout=10)
    return JsonResponse({'status': 200, 'db': db, 'data': payload})