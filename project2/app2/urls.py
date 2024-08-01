from django.urls import path
from . import views

urlpatterns=[
    path('flower/',views.flower,name='flower'),
    path('bag/',views.bag,name='bag'),
    path('mobile/',views.mobile,name='mobile'),
    path('pen/',views.pen,name='pen'),
    path('pencil/',views.pencil,name='pencil'),
    path('notebook/',views.notebook,name='notebook'),
    path('laptop/',views.laptop,name='laptop'),
    path('training/',views.training,name='training'),
    path('college/',views.college,name='college'),
    path('classroom/',views.classroom,name='classroom'),
    path('fan/',views.fan,name='fan'),
    path('computer/',views.computer,name='computer'),
    path('cake/',views.cake,name='cake'),
    path('chocolate/',views.chocolate,name='chocolate'),
    path('coffee/',views.coffee,name='coffee'),
    path('tea/',views.tea,name='tea'),
    path('one/',views.one,name='one'),
    path('two/',views.two,name='two'),
    path('three/',views.three,name='three'),
    path('four/',views.four,name='four')


]