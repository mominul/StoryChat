from django.shortcuts import render, redirect
from chatbot.generate_kids_book_api import SpecalizedChatBot
from bookshelf.models import Books
from django.core.files.base import ContentFile
from django.contrib.auth.models import User
from chatbot.views import home
from fpdf import FPDF

scb=SpecalizedChatBot()
url_data='http://127.0.0.1:8000/books'

# Create your views here.
import requests
def add(request):
    if request.POST:
        pdf_gen = FPDF()
        data = request.session["data"]
        title=request.POST["title"]
        description = request.POST["description"]
        pdf_gen.add_page()
        pdf_gen.set_font('Arial', 'B', 8)
        pdf_gen.multi_cell(0, 10, data)

        pdf_content=pdf_gen.output("random", 'S')
        pdf_content=pdf_content.encode('latin-1')
        file = ContentFile(pdf_content, name="story.pdf")
        print(file)
        author = User.objects.get(id=request.user.pk)
        story = Books(title=title, description=description, pdf=file)
        story.save()
        story.authors.add(author)
        story.save()
        print("saved!")
        return redirect(home)

    return render(request, 'add.html')

def display_books(request):
    respond_data=requests.get(url_data)
    data=None
    if respond_data.status_code==200:
        json_data=respond_data.json()
        data=json_data
    return render(request,'view.html',{'data':data})