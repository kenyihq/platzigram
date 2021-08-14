import json
from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
    now = datetime.now().strftime("%b, %dth, %Y - %H, %M hrs")
    return HttpResponse(f'Oh, hi! current server time is {str(now)}')

def hi(request):
    # numbers = (request.GET["numbers"].split(","))
    numbers = [int(x) for x in request.GET['numbers'].split(',')]
    sorted_int = sorted(numbers)
    print(sorted_int)
    data = {
        'status': 'ok',
        'numbers': sorted_int,
        'message': 'Integers sorted succesfully'
    }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name , age):
    if age < 12:
        message = f'Sorry {name}'
    else:
        message = f'Welcome {name}'

    return HttpResponse(message)
    