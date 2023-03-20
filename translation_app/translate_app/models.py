from django.db import models
from django.contrib.auth.models import User, Group


const_languages = [
    ('Bengali', 'bengali'),
    ('Gujarati', 'gujarati'),
    ('Hindi', 'hindi'),
    ('Kannada', 'kannada'),
    ('Malayalam', 'malayalam'),
    ('Marathi', 'marathi'),
    ('Nepali', 'nepali'),
    ('Oriya', 'oriya'),
    ('Punjabi', 'punjabi'),
    ('Sinhala', 'sinhala'),
    ('Tamil', 'tamil'),
    ('Telugu', 'telugu'),
    ('Urdu', 'urdu'),
]

class Project(models.Model):
    
    wiki_title = models.TextField()
    target_lang = models.CharField(choices=const_languages, max_length=30)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_projects')
    annotator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='annotated_projects', null=True, blank=True)
    
    def get_selected_langs(self):
        for lang in const_languages:
            if lang[1] == self.target_lang:
                return lang[0]
            
    def __str__(self):
        return f"{self.wiki_title}  |  lang - {self.target_lang}"
            
class Sentence(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    original_sentence = models.TextField()
    translated_sentence = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.project.wiki_title}  |  {self.original_sentence}"

# Create your models here.
