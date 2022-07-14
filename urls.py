from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    # path('admin/',admin.site.urls),
    path('',views.SRM),
    path('home',views.home),
    path('signup',views.signup),
    path('login',views.login),
    path('contact',views.contact)
]
