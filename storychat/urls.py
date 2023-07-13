from django.contrib import admin
from django.urls import path, include
from chatbot.views import home, chat_clear

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('chat/clear', chat_clear, name="clear_chat")
]