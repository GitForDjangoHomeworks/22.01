from django.db import models
from django.utils.translation import gettext_lazy as _
from .validator import validate_even


# Create your models here.

class MyModel(models.Model):
    CHOICES = (
        ('US', 'United States'),
        ('FR', 'France'),
        ('CN', 'China'),
        ('RU', 'Russia'),
        ('UZ', 'Uzbekistan'),
        ('IT', 'Italy'),
    )
    title = models.CharField(verbose_name='title', max_length=255)
    desc = models.CharField(verbose_name='desc', max_length=255)
    number = models.IntegerField(verbose_name='number', validators=[validate_even])
    choice = models.CharField(max_length=300, choices=CHOICES)

    def __str__(self):
        return f'{self.title} {self.pk+self.number}'