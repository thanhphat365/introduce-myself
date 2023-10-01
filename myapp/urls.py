from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('home/',views.home, name='home'),
    path('skill',views.skill),
    path('about',views.about)
]
