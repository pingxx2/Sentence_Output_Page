from django.shortcuts import render, get_object_or_404
from .models import Sentence
from django.utils import timezone
import random

def index(request):
    """
    문구 출력
    """
    s_get = Sentence.objects.all()
    size = s_get.count()
    
    sentence = get_object_or_404(Sentence, id=random.randrange(1,size))
    context = {'sentence':sentence}
    return render(request, 'main/index.html', context)
