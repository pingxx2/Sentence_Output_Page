from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from common.forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})
<<<<<<< HEAD

=======
"""
>>>>>>> fb34df3c6a43ffedf2cbd4bb1681faed620fab51
@login_required(login_url='common:login')
def bookmark(request):
    sentence = get_object_or_404(User, id=request.user.id)
    bookmark_list = sentence.bookmark.all()
    messages.success(request, bookmark_list)
    #bookmark_list = sentence.bookmark

    context = {'bookmark_list':bookmark_list}

<<<<<<< HEAD
    return render(request, 'main/bookmark.html', context)
=======
    return render(request, 'main/bookmark.html', context)
"""
>>>>>>> fb34df3c6a43ffedf2cbd4bb1681faed620fab51
