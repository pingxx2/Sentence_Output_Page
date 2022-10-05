from django.shortcuts import render, get_object_or_404
from .models import Sentence
from django.utils import timezone

def index(request):
    """
    문구 출력
    """
    sentence = get_object_or_404(Sentence)
    context = {'sentence':sentence}
    return render(request, 'main/index.html', context)
