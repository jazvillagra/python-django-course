from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    my_dict = {'help_page': "Help Page under construction"}
    return render(request, 'django_app/index.html', context=my_dict)

# Create your views here.
