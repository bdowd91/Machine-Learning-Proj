from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def movies(request):
    sample_dict = {
        'insert_me':'Hello I am from views.py!'
    }
    return render(request,'index.html',context=sample_dict)