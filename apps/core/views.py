from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from .models import Userprofile

def frontpage(request):
    return render(request, 'core/frontpage.html')

def contact(request):
    return render(request, 'core/contact.html')

def about_me(request):
    return render(request, 'core/about_me.html')



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = user.username
            user.save()

            userprofile = Userprofile.objects.create(user=user)

            login(request, user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})