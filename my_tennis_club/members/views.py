from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from .forms import MemberForm


# Create your views here.
#def myFirst(request):
#    mymembers = Member.objects.all().values()
#    temp=loader.get_template('myFirst.html')
 #   context = {
        # 'firstname':'Aarti'
  #      'mymembers':mymembers,
   # }
    #return HttpResponse(temp.render(context,request))

def myFirst(request):
    context={}
    form=MemberForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
    context['form']=form
            
    return render(request,"myFirst.html",context)  