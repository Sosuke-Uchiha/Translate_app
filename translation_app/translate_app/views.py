from django.shortcuts import render
from . import models
from wikipediaapi import Wikipedia 
from django.http import HttpResponse
import nltk
from nltk.tokenize import sent_tokenize
from .models import const_languages
from django.contrib.auth.models import Group
import json



def add_project(request):
            
    if request.method == 'POST':
        title = request.POST['wiki_title']
        target_lang = request.POST['target_lang']
        
        
        #separate para into sentences
        
        try:
            intro = Wikipedia().page(title).summary
        except Exception as e:
            print(e)
            return HttpResponse(e)
        
        nltk.download('punkt')
        sentences = sent_tokenize(intro)

        existing_project = models.Project.objects.filter(
            wiki_title = title,
            target_lang = target_lang
        )
        
        if existing_project:
            return HttpResponse('Project Already exists.')
        else:
            project = models.Project.objects.create(
                wiki_title = title,
                target_lang = target_lang,
                created_by = request.user
            )
            
            for sentence in sentences:
                models.Sentence.objects.create(
                    project = project,
                    original_sentence = sentence
                )
                
    context = {
        'langs' : const_languages
    }
    
    return render(request, 'add_project.html', context)
            
        
def dashboard(request):
    projects = models.Project.objects.all()
    
    manager = True
    manager_group = Group.objects.get(name="Manager")
    if manager_group not in request.user.groups.all():
        projects = projects.filter(annotator=request.user.id)
        manager = False
        
    context = {
        'projects' : projects,
        'manager'  : manager
    }
    return render(request, "dashboard.html", context)

def project(request, id):
    
    sentences = models.Sentence.objects.filter(project__id=id)
    project = models.Project.objects.filter(id=id).first()
    
    if not project:
        return HttpResponse("No project with the given id")
    
    manager = True
    manager_group = Group.objects.get(name="Manager")
    if manager_group not in request.user.groups.all():
        manager = False
    
    context = {
        'sentences' : sentences,
        'project' : project,
        'manager' : manager
    }
    
    if request.method == 'POST':
        for sent_id, translated_sent in request.POST.items():
            if sent_id != 'csrfmiddlewaretoken':
                sentence = models.Sentence.objects.filter(project__id=id, id=int(sent_id)).first()
                sentence.translated_sentence = translated_sent
                sentence.save()
            
                
    return render(request, 'project.html', context )
