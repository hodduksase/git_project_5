from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    if request.method == 'POST':
        # Here you would typically handle the form submission
        # For now, we'll just return a success message
        return HttpResponse('Thank you for your message! We will get back to you soon.')
    return render(request, 'contact.html')
