from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def view_red(request):
    temp=loader.get_template("red.html")
    return HttpResponse(temp.render())

def view_pink(request):
    temp=loader.get_template("pink.html")
    return HttpResponse(temp.render())

def view_burlywood(request):
    temp=loader.get_template("burlywood.html")
    return HttpResponse(temp.render())

def view_brown(request):
    temp=loader.get_template("brown.html")
    return HttpResponse(temp.render())

def view_blueVoilet(request):
    temp=loader.get_template("blueVoilet.html")
    return HttpResponse(temp.render())  

def view_blue(request):
    temp=loader.get_template("blue.html")
    return HttpResponse(temp.render()) 

def view_bisque(request):
    temp=loader.get_template("bisque.html")
    return HttpResponse(temp.render())               

def view_aquamarine(request):
    temp=loader.get_template("aquamarine.html")
    return HttpResponse(temp.render())

def view_aqua(request):
    temp=loader.get_template("aqua.html")
    return HttpResponse(temp.render())

def view_Antiquewhite(request):
    temp=loader.get_template("Antiquewhite.html")
    return HttpResponse(temp.render())

def view_black(request):
    temp=loader.get_template("black.html")
    return HttpResponse(temp.render())

def view_blanchedalmond(request):
    temp=loader.get_template("blanchedalmond.html")
    return HttpResponse(temp.render())
               
def view_chartreuse(request):
    temp=loader.get_template("chartreuse.html")
    return HttpResponse(temp.render())


def view_coral(request):
    temp=loader.get_template("coral.html")
    return HttpResponse(temp.render())

def view_chocolate(request):
    temp=loader.get_template("chocolate.html")
    return HttpResponse(temp.render())
    
def view_cadetblue(request):
    temp=loader.get_template("cadetblue.html")
    return HttpResponse(temp.render())

def view_azure(request):
    temp=loader.get_template("azure.html")
    return HttpResponse(temp.render())

def view_cornflowerblue(request):
    temp=loader.get_template("cornflowerblue.html")
    return HttpResponse(temp.render())

def view_crimson(request):
    temp=loader.get_template("crimson.html")
    return HttpResponse(temp.render())
   
def view_cornsilk(request):
    temp=loader.get_template("cornsilk.html")
    return HttpResponse(temp.render())



def test(request):
    return HttpResponse("<h1>Test function of app1 called</h1>")

def laptop(request):
    return HttpResponse("<h1>This Laptop function of app1 called </h1>")    
def fan(request):
    return HttpResponse("<h1> Hello Fan</h1>")