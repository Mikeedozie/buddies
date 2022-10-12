from django.shortcuts import render
from .models import Member, SpecialityTags, Topic, Quiz


# Create your views here.

def index(request):
    members = Member.objects.all()
    topics = Topic.objects.all()
    context = {'members': members, 'topics': topics}
    return render(request, 'index.html', context)

def topic(request, id):
    topic = Topic.objects.get(id=id)
    context = {'topic': topic}
    return render(request, 'topic.html', context)