from django.conf.urls import url
from . import views

urlpatterns = [
   
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name='register'),
    url(r'conversion/$', views.conversion, name = 'conversion'),
]
