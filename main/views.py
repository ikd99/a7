from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import requests, user_info, favorite, messages
from .form import PostAdd, TestForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = requests.objects.all()
    users = user_info.objects.all()
    header = ['ID','タイトル','目的地','出発地','日付','テキスト']
    my_dict2 = {
        'title':'タイトル',
        'posts': posts,
        'users': users,
        'header': header,
    }
    return render(request, 'main/index.html', my_dict2)


def post(request):
    message = ''
    if (request.method == 'POST'):
        form = PostAdd(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(to='/')
        else:
            message = "再入力してください"
    modelform_dict = {
        'title':'依頼投稿ページ',
        'form': PostAdd(),
        'message': message,
    }
    return render(request, 'main/post.html', modelform_dict)

def getMyPage(request):
    header = ['ユーザー名', 'ドライバーか', '地域']
    my_dict ={
        'header': header,
        'user' : user_info.objects.get(id=1),
        'favorite': favorite.objects.get(id=1)
    }
    return render(request, 'main/mypage.html', my_dict)

@login_required
def chat(request, num):
    chat_room = requests.objects.get(id=num)
    comment = messages.objects.all().filter(post_id=chat_room.id)
    
    my_dict = {
        'form': TestForm,
        'comment': comment,
        'id': chat_room.id,
    }
    print(chat_room.id)
    print(num)
    print(request.user)
    if (request.method == "POST"):
        my_dict['form'] = TestForm(request.POST)
        user = request.user
        # user = User.objects.get(id=user_id)
        # messages.user_id = request.user
        # messages.post_id = chat_room.id
        # messages.text = request.POST['text']
        # messages.save()
        post_comment = messages(user_id=user, post_id = chat_room, text=request.POST['text'])
        post_comment.save()
        return HttpResponseRedirect('chat')
    return render(request, 'main/chat.html', my_dict)
