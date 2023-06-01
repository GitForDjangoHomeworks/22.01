from django.shortcuts import render, HttpResponse
from .models import MyModel
import random

# Create your views here.

def add_models(request, pk=None):
    new_single_model = MyModel.objects.create(title='single', desc='single_desc', number='1', choice=MyModel.CHOICES[random.randint(0, len(MyModel.CHOICES))])
    new_single_model.save()


    create_list = [
        {'title': 'cycle1', 'desc': 'cycle_desc1', 'number': '5', 'choice': MyModel.CHOICES[random.randint(0, len(MyModel.CHOICES) - 1)]},
        {'title': 'cycle2', 'desc': 'cycle_desc2', 'number': '6', 'choice': MyModel.CHOICES[random.randint(0, len(MyModel.CHOICES) - 1)]},
        {'title': 'cycle3', 'desc': 'cycle_desc3', 'number': '7', 'choice': MyModel.CHOICES[random.randint(0, len(MyModel.CHOICES) - 1)]},
    ]

    for i in create_list:
        new_model = MyModel.objects.create(title=i['title'], desc=i['desc'], number=i['number'], choice=i['choice'])
        new_model.save()
        
    context = {1: 1}
       
    return render(request=request, template_name='index.html', context=context)
