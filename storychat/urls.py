from django.contrib import admin
from django.urls import path
from chatbot.views import home_view, welcome
from authentication.views import login_page, logout_page, signup_view

urlpatterns = [
    path('', welcome, name='welcome'),
    path('home/', home_view, name='home'),
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('signup/', signup_view, name='signup'),
    path('admin/', admin.site.urls),
    # path('', include('chatbot.urls')),
    # path('', include('authentication.urls')),
    
]