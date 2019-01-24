from django.http import HttpResponse, JsonResponse

from _datetime import datetime


def hello_word(request):
    """Return a greeting"""

    now = datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    return HttpResponse('Hola mundo 2 {now}'.format(now=now))


def sort_integers(request):
    """"return"""

    print("hola")
    numbers = [int(i) for i in sorted(request.GET['numbers'].split(','))]


    return JsonResponse({'a': numbers })


def say_hi(request, name, age):

    if age < 12 :
        message = "Sorry {name}, you are not allowed here".format(name=name)
    else:
        message = "Hello, {name}!, Welcome to Platzi".format(name=name)


    return HttpResponse(message)
