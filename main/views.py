from django.shortcuts import render, get_object_or_404, redirect
from .models import Sentence
import random
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def index(request):
    """
    문구 출력
    """
    heart = 0
    if request.method == 'POST':
        sentence_id = request.POST.get('id_value')
        sentence = get_object_or_404(Sentence, pk=sentence_id, id=sentence_id)
        try:
            check = get_object_or_404(Sentence, bookmark=request.user, pk=sentence_id, id=sentence_id)
            sentence.bookmark.remove(request.user)
            heart=0
        except TypeError:
            # 로그인없이 하트 눌렀을 때 , 로그인 창으로 이동
            return redirect('common:login')
        except:
            sentence.bookmark.add(request.user)
            heart=1
        context = {'sentence':sentence, 'heart':heart}
        return render(request, 'main/index.html', context)
        #return redirect('main:index')
    else:
        s_get = Sentence.objects.all()
        size = s_get.count()
        random_num = random.randrange(1,size)
        sentence = get_object_or_404(Sentence, id=random_num)
        try:
            check = get_object_or_404(Sentence, bookmark=request.user, id=random_num)
            heart=1
        except:
            heart=0
        context = {'sentence':sentence, 'heart':heart}
        return render(request, 'main/index.html', context)

"""
@login_required(login_url='common:login')
def bookmark(request):
    sentence = get_object_or_404(Sentence, id=request.user.id)
    bookmark_list = sentence.bookmark.all()
    messages.success(request, bookmark_list)
    #bookmark_list = sentence.bookmark

    context = {'bookmark_list':bookmark_list}

    return render(request, 'main/bookmark.html', context)

"""
