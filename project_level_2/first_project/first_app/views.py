from django.shortcuts import render
from first_app.models import Users

# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def users(request):
    users_list = Users.objects.all().order_by('first_name')
    context_dict = {'users': users_list}
    return render(request, 'first_app/users.html', context=context_dict)
