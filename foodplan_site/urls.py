from django.urls import path
from foodplan_site import views

urlpatterns = [
    path('', views.index, name='index')
]
