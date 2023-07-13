from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from chatbot.models import Snippet
# from chatbot.serializers import SnippetSerializer

def home(request):
    return render(request, 'home.html')