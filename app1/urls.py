from django.urls import path
from .views import index,article,nav
urlpatterns=[
    path('',index,name="home"),
    path('two/<int:id>',article,name="article"),
    path('nav',nav),
]