from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.login, name='login'),

    url(r'^send_message.html/$', views.send_message, name='send_message'),
    url(r'^about.html/$', views.about),
    url(r'^history.html/$', views.history),
    url(r'^register/$', views.register),
]
