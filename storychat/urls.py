from django.contrib import admin
from django.urls import path
from authentication.views import login_page, logout_page, signup_view
from django.urls import path, include
from bookshelf.views import books_list, books_detail
from chatbot.views import home, chat_clear, welcome

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('chat/clear', chat_clear, name="clear_chat"),
    path("books/", books_list, name="books_list"),
    path("books/<int:book_id>", books_detail, name="books_detail")
]