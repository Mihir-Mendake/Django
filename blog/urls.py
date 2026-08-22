from django.http import HttpResponse
from django.urls import path
from . import views

#     path('allposts/python_intro',views.python_intro),
#     path('allposts/django_basic',views.django_basics),
#     path('allposts/python_oops',views.python_oops),

urlpatterns = [
    path('',views.home_page, name="home"),
    path('allposts', views.blogposts),
    #path("allposts/<int:blog>", views.blog_post_by_number),
    path("allposts/<slug:blog>",views.blog_post, name="blog-post"),

]


