from django.db import models

PRIORITY=[('H','high'),('M','Medium'),('L','low'),]

class Question(models.Model):
    title                   =models.CharField(max_length=60)
    question                =models.TextField(max_length=400)
    priority                =models.CharField(max_length=1, choices=PRIORITY)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="The question"
        verbose_name_plural="people question"


# Create your models here.
