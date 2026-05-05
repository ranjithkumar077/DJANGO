from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderabad(request):
    name="tony"
    context={"name":name,
             "age":18}
    res="<h1> hello </h1>"
    return render(request,"hyderabad.html",context)
def warangal(request):
    name="tony"
    context={"name":name,
             "age":38}
    res="<h1> hello </h1>"
    return render(request,"warangal.html",context)
