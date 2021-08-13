from django.urls import path
from platzigram import view

urlpatterns = [
    
    path('hello/', view.hello_world) 

]
