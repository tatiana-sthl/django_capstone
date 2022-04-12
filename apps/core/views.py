from django.shortcuts import render

def frontpage(request):
    return render(request, 'core/frontpage.html')

def contact(request):
    return render(request, 'core/contact.html')

def about_me(request):
    return render(request, 'core/about_me.html')
