from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('answer', views.ans, name = 'ans')
]