from django.urls import path
from . import views

urlpatterns = [
    path('', views.personal),
    path('cv/', views.cv),
    path('shopping', views.shopping)
]
