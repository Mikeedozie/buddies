from django.shortcuts import render
from .models import Member, SpecialityTags, Topic, Quiz


# Create your views here.

def index(request):
    members = Member.objects.all()
    topics = Topic.objects.all()
    context = {'members': members, 'topics': topics}
    return render(request, 'index.html', context)