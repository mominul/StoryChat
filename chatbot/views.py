from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .generate_orca_mini import generate_orc
from .models import ChatHistory
from .generate_kids_book_api import SpecalizedChatBot
scb=SpecalizedChatBot()

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
        history.user.add(user)
        return redirect(home)
    
    history = ChatHistory.objects.filter(user=user)
    print()
    items = []
    for item in history:
        items.append({
            "prompt": item.prompt,
            "response": item.response,
        })
    try:
        request.session["data"] = items[-1]["response"]
    except:
        request.session["data"] = ""
    data = {
        "name": user.first_name,
        "history": items,
    }

    return render(request, 'home.html', data)

def chat_clear(request):
    user = request.user
    ChatHistory.objects.filter(user=user).delete()
    return redirect(home)

def chat_story_api(request):
    prompt=request.GET.get('prompt','')
    pdf_content=scb.generate_response(prompt)
    pdf_content=pdf_content.encode('latin-1')
    response=HttpResponse(content_type='application/pdf')
    response['Content-Disposition']='attachment; filename="file.pdf"'
    response.write(pdf_content)
    return response
