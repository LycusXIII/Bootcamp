from django.contrib import admin
from .models import Question, Choice

# Register your models here
# Registers the Question, Choice models
admin.site.register(Question)
admin.site.register(Choice)

# The Task did not ask for the choice model to be registered
