from django.urls import path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('tutor/', views.tutor, name="tutor"),
    path('contact/', views.contact, name="contact"),
    path('request/', views.ReqHelp.as_view(), name="request"),
    path('values/', views.Eren.as_view(), name="values"),
]