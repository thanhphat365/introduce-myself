from django.shortcuts import render
from .models import Home
# Create your views here.
def home(request):
    homes = Home.objects.all().order_by("date")
    context = {
        'homes': homes,
    }
    return render(request, 'page/home.html', context)
    
#skill
def skill(request):
    return render(request, 'page/skill.html')

def about(request):
    return render(request, 'page/about.html')
    