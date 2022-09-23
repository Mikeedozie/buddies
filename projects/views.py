from django.shortcuts import render
from .models import Member, ProfileImage, SpecialityTags


# Create your views here.

def index(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'index.html', context)