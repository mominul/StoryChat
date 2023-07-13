from django.contrib import admin
from django.urls import path, include
from chatbot.views import home, chat_clear
from bookshelf.views import books_list, books_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('chat/clear', chat_clear, name="clear_chat"),
    path("books/", books_list, name="books_list"),
    path("books/<int:book_id>", books_detail, name="books_detail")
]