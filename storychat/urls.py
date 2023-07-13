from django.contrib import admin
from django.urls import path, include
from chatbot.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot.urls')),
]