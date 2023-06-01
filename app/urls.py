from django.urls import path, include
from .views import add_models

app_name = 'app'

urlpatterns = [
    path('index/', add_models, name='asdasd')
]
