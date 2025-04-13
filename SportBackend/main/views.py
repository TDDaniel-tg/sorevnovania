from django.shortcuts import render

def home(request):
    return render(request, 'main/index.html')

def male_standards(request):
    return render(request, 'main/male.html')

def female_standards(request):
    return render(request, 'main/female.html')

def disciplines(request):
    return render(request, 'main/disciplin.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html') 