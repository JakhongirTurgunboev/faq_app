from django.shortcuts import render
from .models import Subject, Topic

def index(request):
    subjects_with_topics = []
    subjects = Subject.objects.all()
    for subject in subjects:
        topics = subject.topic_set.all()  # Retrieve related topics for the current subject
        subjects_with_topics.append({'subject': subject, 'topics': topics})
    return render(request, 'index.html', {'subjects_with_topics': subjects_with_topics})

def topic_detail(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    return render(request, 'topic_detail.html', {'topic': topic})
