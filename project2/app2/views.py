from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def flower(request):
    return HttpResponse("<h1>Flower function of app2 is called</h1>")

def bag(request):
    return HttpResponse("<h2>My bag is black in color<h2>")

def mobile(request):
    return HttpResponse("<h3>Mobile function of app2 is in views</h3>")

def pen(request):
    return HttpResponse("<h4>I have a pen</h4>")

def pencil(request):
    return HttpResponse("<h5>This is a pencil function</h5>") 

def notebook(request):
    return HttpResponse("<h6>This is my Notebook</h6>")  

def laptop(request):
    return HttpResponse("Laptop function is in app2")

def training(request):
    return HttpResponse("We have our training starts from tommrow")

def college(request):
    return HttpResponse("This is college function")

def classroom(request):
    return HttpResponse("This is a classroom function")

def fan(request):
    return HttpResponse("This is fan function")

def computer(request):
    return HttpResponse("This is a computer function")         

def cake(request):
    return HttpResponse("I like chocolate cakes")
               
def chocolate(request):
    return HttpResponse("This is chocolate functioon in app2")

def cake(request):
    return HttpResponse("I like chocolate cakes")

def coffee(request):
    return HttpResponse("coffee function of app2 is called")

def tea(request):
    return HttpResponse("tea function of app2 is called")

def one(request):
    return HttpResponse("one function of app2 is called")

def two(request):
    return HttpResponse("two function of app2 is called")

def three(request):
    return HttpResponse("three function of app2 is called")

def four(request):
    return HttpResponse("four function of app2 is called")                    
