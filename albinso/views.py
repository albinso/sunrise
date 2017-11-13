from django.http import HttpResponse


def index(request):
    return HttpResponse("We're live from the internet!")