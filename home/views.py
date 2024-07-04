from django.shortcuts import render

# Create your views here.

    
def home__view(request):
    return render(request,'home.html')
