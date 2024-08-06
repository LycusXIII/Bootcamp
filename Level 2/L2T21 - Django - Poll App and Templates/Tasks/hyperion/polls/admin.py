from django.contrib import admin
from .models import Question, Choice

# Register your models here
# Registers the Question, Choice models
admin.site.register(Question)
admin.site.register(Choice)
