from django.contrib import admin
from django.urls import path, include
from . import views
from .views import AgileDetail

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('archive/', views.article_index, name='archive'),
    path('<str:pk>/', views.singleAgile, name='agile_id'),
    # path('accounts/login/', views.article_index, name='archive_login'),
]