import textwrap

from django.http import JsonResponse
import json
import datetime

def hello(request):
    print str(request)
    #request.
    name = request.GET.get('name') or "UNKNOWN"
    return JsonResponse({'data':'hello! '+ name, 'time': datetime.datetime.now(),'tip': 'use ?name=bar to assign a name'})
