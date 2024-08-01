from django.urls import path
from . import views

urlpatterns=[
    path('test/',views.test,name='test'),
    path('laptop/',views.laptop,name='laptop'),
    path('fan/',views.fan,name='fan'),
    path('view_red/',views.view_red,name='view_red'),
    path('view_pink/',views.view_pink,name='view_pink'),
    path('view_burlywood/',views.view_burlywood,name='view_burlywood'),
    path('view_brown/',views.view_brown,name='view_brown'),
    path('view_blueVoilet/',views.view_blueVoilet,name='view_blueVoilet'),
    path('view_blue/',views.view_blue,name='view_blue'),
    path('view_bisque/',views.view_bisque,name='view_bisque'),
    path('view_aquamarine/',views.view_aquamarine,name='view_aquamarine'),
    path('view_aqua/',views.view_aqua,name='view_aqua'),
    path('view_Antiquewhite/',views.view_Antiquewhite,name='view_Antiquewhite'),
    path('view_black/',views.view_black,name='view_black'),
    path('view_cornsilk/',views.view_cornsilk,name='view_cornsilk'),
    path('view_blanchedalmond/',views.view_blanchedalmond,name='view_blanchedalmond'),
    path('view_chartreuse/',views.view_chartreuse,name='view_chartreuse'),
    path('view_coral/',views.view_coral,name='view_coral'),
    path('view_chocolate/',views.view_chocolate,name='view_chocolate'),
    path('view_cadetblue/',views.view_cadetblue,name='view_cadetblue'),
    path('view_azure/',views.view_azure,name='view_azure'),
    path('view_cornflowerblue/',views.view_cornflowerblue,name='view_cornflowerblue'),
    path('view_crimson/',views.view_crimson,name='view_crimson')
    

]

