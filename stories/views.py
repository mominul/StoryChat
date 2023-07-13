from django.shortcuts import render

# Create your views here.
def add(request):
    print(request.session["data"])
    return render(request, 'add.html')