from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chittoor(request):
    name="tony"
    age=30
    context={"name":name,
             "age":age}
    res="<h1> hello </h1>"
    return render(request,"chittoor.html",context)

def kadapa(request):
    name="tony"
    context={"name":name,
             "age":10}
    res="<h1> hello </h1>"
    return render(request,"kadapa.html",context)