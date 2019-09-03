from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index),
    path('wt', views.what),
    path('gg',views.ggcall),
    path('admin/', admin.site.urls),
]