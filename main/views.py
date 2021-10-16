# from typing_extensions import Required
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from .models import requests, user_info, favorite, messages
from .form import PostAdd, TestForm, PostForm, UserForm
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

@login_required
def post(request):
    message = ''
    my_dict = {
        'form': PostForm,
        'message': message,
    }
    if (request.method == "POST"):
        my_dict['form'] = PostForm(request.POST)
        print(my_dict['form'])
        user = request.user
        post = requests(
            client_id=user, 
            title=request.POST.get('title'), 
            text=request.POST.get('text'),
            departure_place=request.POST.get('departure_place'),
            destination_place=request.POST.get('destination_place'),
            delivery_date=request.POST.get('delivery_date'),
            asking_price=request.POST.get('asking_price'),
        )
        post.save()
        return redirect('main:post')
    return render(request, 'main/post.html', my_dict)


def mypage(request):
    # header = ['ユーザー名', 'ドライバーか', '地域']
    # my_dict ={
    #    'header': header,
    #    'user' : user_info.objects.get(id=1),
    #    # 'favorite': favorite.objects.get(id=1)
    #}
    # return render(request, 'main/mypage.html', my_dict)
    return render(request, "main/mypage.html")

@login_required
def profile(request):
    user = request.user
    all_user = user_info.objects.all().filter(user_name=user)
    use_dict = {
        'form': UserForm,
        "all_user_info": all_user,
    }
    if request.method == 'POST':
        use_dict['form'] = UserForm(request.POST)
        #user = request.user
        print(use_dict['form'])
        print(request.POST('is_driver'))
        print(request.POST.get('region'))
        post = requests(
            # user_name=user, 
            is_driver=request.POST('is_driver'), 
            region=request.POST('region'),
            # total_socore=request.POST.get('total_socore'),
        )
        post.save()
        return redirect('main:profile')
    return render(request, "main/profile.html", use_dict)

def getMyPage(request):
    return render(request, 'main/mypage.html')

@login_required
def chat(request, num):
    chat_room = requests.objects.get(id=num)
    comment = messages.objects.all().filter(post_id=chat_room.id)  
    header = ['ユーザー','内容']
    my_dict = {
        'form': TestForm,
        'comment': comment,
        'id': chat_room.id,
        'header': header,
    }
    print(chat_room.id)
    print(num)
    print(request.user)
    if (request.method == "POST"):
        my_dict['form'] = TestForm(request.POST)
        user = request.user
        post_comment = messages(user_id=user, post_id = chat_room, text=request.POST['text'])
        post_comment.save()
        return redirect('main:chat',  num=num)
    return render(request, 'main/chat.html', my_dict)

def message(request):
    return render(request, 'main/message.html')
