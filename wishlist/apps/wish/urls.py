from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^home$', views.home),
    url(r'^login', views.loginUser),
    url(r'^logout', views.logout),
    url(r'^register$', views.registerUser)
]