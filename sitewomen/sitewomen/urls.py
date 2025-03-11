from django.contrib import admin
from django.urls import path
from women.views import index, categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('categories/', categories),
]
