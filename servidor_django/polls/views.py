from django.http import HttpResponse


def index(request):
    return HttpResponse("Hey, como mola, estoy aqui.")


def patata(request):
    return HttpResponse("Hey, hola patata")
