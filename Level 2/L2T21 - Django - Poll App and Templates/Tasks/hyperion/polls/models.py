from django.db import models


# Create your models here.
class Question(models.Model):
    '''This class defines the data types
    for question_text and pub_date'''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        '''Returns the question text'''
        return self.question_text


class Choice(models.Model):
    '''This class defines the data types
    for question, choice_text and votes'''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        '''Returns the choice text'''
        return self.choice_text
