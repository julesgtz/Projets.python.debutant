from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('<str:short_url>/', views.redirect),
]