from django.shortcuts import render


# Create your views here.
def blog1():
    response="<h1>this is BLOG 1</h1>"
    return HttpResponse(response)
def blog2():
    response="<h1>this is BLOG 1</h1>"
    return HttpResponse(response)