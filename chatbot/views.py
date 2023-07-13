from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .generate_orca_mini import generate_orc
from .models import ChatHistory

def welcome(request):
    if request.user.is_authenticated:
        return redirect(home)
    return render(request,'welcome.html')

@login_required
def home(request):
    user = User.objects.get(id=request.user.pk)
    if request.POST:
        chat = request.POST["chat"]
        response = generate_orc(chat).removeprefix("1. ")
        history = ChatHistory(prompt=chat, response=response)
        history.save()
        print(response)
        return redirect("/")
    
    history = ChatHistory.objects.all()
    print()
    items = []
    for item in history:
        items.append({
            "prompt": item.prompt,
            "response": item.response,
        })
    data = {
        "name": user.first_name,
        "history": items,
    }

    return render(request, 'home.html', data)

def chat_clear(request):
    ChatHistory.objects.all().delete()
    return redirect("/")
