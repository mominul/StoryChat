from django.shortcuts import render
from .models import Books
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

def search_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        results = Books.objects.filter(title__icontains=title)
        return render(request, 'search_results.html', {'results': results})
    else:
        return render(request, 'search_book.html')
    

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def books_list(request):
    if (request.method == "GET"):
        data = serializers.serialize("json", Books.objects.all())
        return JsonResponse(json.loads(data), safe=False)

    if (request.method == "POST"):
        body = json.loads(request.body.decode("utf-8"))
        newrecord = Books.objects.create(item=body['item'])
        # Turn the object to json to dict, put in array to avoid non-iterable error
        data = json.loads(serializers.serialize('json', [newrecord]))
        # send json response with new object
        return JsonResponse(data, safe=False)

@csrf_exempt ## To exempt from default requirement for CSRF tokens to use postman
def books_detail(request, id):
        if (request.method == "PUT"):
        # Turn the body into a dict
            body = json.loads(request.body.decode("utf-8"))
        # update the item
            Books.objects.filter(pk=id).update(item=body['item'])
            newrecord = Books.objects.filter(pk=id)
        # Turn the object to json to dict, put in array to avoid non-iterable error
            data = json.loads(serializers.serialize('json', newrecord))
        # send json response with updated object
            return JsonResponse(data, safe=False)

        if (request.method == "DELETE"):
        # delete the item, get all remaining records for response
            Books.objects.filter(pk=id).delete()
            newrecord = Books.objects.all()
            data = json.loads(serializers.serialize('json', newrecord))
            return JsonResponse(data, safe=False)
