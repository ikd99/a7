from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import requests, user_info, favorite, messages
from .form import PostAdd, TestForm, PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = requests.objects.all()
    header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
    my_dict2 = {
        'posts': posts,
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

def detail(request, num):
    posts = requests.objects.all().filter(id=num)
    header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
    my_dict = {
        'id': num,
        'posts': posts,
        'header': header,
    }
    return render(request, 'main/detail.html', my_dict)