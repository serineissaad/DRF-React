from django.shortcuts import render

# Create your views here.

def index(request, *args, **kwargs):
    #return render(request, 'react/blogapi/templates/frontend/index.html')
    return render(request, 'frontend2/public/index.html')