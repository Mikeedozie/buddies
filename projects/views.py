from django.shortcuts import render
from .models import Member, SpecialityTags


# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)