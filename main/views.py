from django.shortcuts import render, get_object_or_404, redirect
from .models import Sentence
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    """
    문구 출력
    """
    s_get = Sentence.objects.all()
    size = s_get.count()
    random_num = random.randrange(1,size)
    sentence = get_object_or_404(Sentence, id=random_num)
    context = {'sentence':sentence, 'random_num':random_num}
    return render(request, 'main/index.html', context)


@login_required(login_url='common:login')
def vote_bookmark(request, sentence_id):
    """
    즐겨찾기 등록
    """
    heart = 0
    sentence = get_object_or_404(Sentence, pk=sentence_id, id=sentence_id)
    try:
        check = get_object_or_404(Sentence, bookmark=request.user, pk=sentence_id, id=sentence_id)
        sentence.bookmark.remove(request.user)
        heart=0
    except:
        sentence.bookmark.add(request.user)
        heart=1
    context = {'sentence':sentence, 'heart':heart}
    return render(request, 'main/index.html', context)
    