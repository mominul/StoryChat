from django.contrib import admin
from django.urls import path
from authentication.views import login_page, logout_page, signup_view
from django.urls import path, include
from bookshelf.views import books_list, books_detail, search_book
from chatbot.views import home, chat_clear, welcome, chat_story_api
from stories.views import add
from stories.views import display_books
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('admin/', admin.site.urls),
    # path('', home, name='home'),
    path('chat/clear', chat_clear, name="clear_chat"),
    path("books/", books_list, name="books_list"),
    path("books/<int:book_id>", books_detail, name="books_detail"),
    path('add/',add, name='add'),
    path('download/', chat_story_api),
    path('display_books/',display_books),
    path('search', search_book, name='search' )
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)