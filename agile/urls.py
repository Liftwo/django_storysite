from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('archive/', views.article_index, name='archive'),
    path('<int:pk>/', views.singleAgile, name='agile_id'),
    path('login_custom/', views.post_login, name='login_custom'),
    path('logout/', views.post_logout, name='logout'),
    path('register_create/', views.register_create_view, name='register_create'),
    path('show_register/', views.show_register, name='show_register'),
    path('test/', views.test),
    path('forgotpwd', views.forgot_pwd_view, name='forgotpwd'),

]