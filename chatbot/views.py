from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# from rest_framework.parsers import JSONParser
# from chatbot.models import Snippet
# from chatbot.serializers import SnippetSerializer
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    data = {
        'name': request.user.get_full_name(),
        'fname': request.user.first_name, 
        'lname': request.user.last_name
        }
    print(data)
    return render(request, 'home.html', data)

def welcome(request):
    return render(request, 'welcome.html')