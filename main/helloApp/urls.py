from django.urls import path

from . import views

app_name = 'helloApp'
urlpatterns = [
    path('', views.index, name='index')
]
