from django.shortcuts import render
from django.http import HttpResponse
from .models import Details

def members(request):
    return HttpResponse("Hello world!")

def index(request):
    if request.method == 'POST':
        type = request.POST['type']
        name = request.POST['name']
        print(type, name)
        obj=Details()
        obj.name = name
        obj.type = type
        obj.save()

    #fetching details and saving in dictionary
    from django.core import serializers
    data=serializers.serialize("python", Details.objects.all())

    context = {
        'data': data,
    }

    return render(request,'index.html', context)

def next(request):
    return render(request,'anotherpage.html')
