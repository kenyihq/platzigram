from django.urls import path
from platzigram import view as local_views
from posts import views as post_views

urlpatterns = [
    
    path('hello/', local_views.hello_world),
    path("hi/", local_views.hi) ,
    path("say-hi/<str:name>/<int:age>", local_views.say_hi),

    path('posts/', post_views.list_posts)

]
