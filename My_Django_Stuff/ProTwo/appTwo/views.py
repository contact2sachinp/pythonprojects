from django.shortcuts import render
from django.http import HttpResponse
#from appTwo.models import User

from appTwo.forms import NewUserForm

# Create your views here.

def index(request):
    #return HttpResponse('<em> My Second Project Test </em>')
    return render(request, 'appTwo/index.html')

def users(request):
    """
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/users.html', context=user_dict)
    """
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Invalid Form details')

    return render(request, 'appTwo/users.html', {'form':form})

def help(request):
    helpDict = {'help_insert':'HELP PAGE TEST'}
    return render(request, 'appTwo/help.html', context=helpDict)