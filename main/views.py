from django.shortcuts import redirect, render
from .models import requests, user_info, favorite
from .form import PostAdd

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

def chat(request):
    return render(request, 'main/chat.html')
