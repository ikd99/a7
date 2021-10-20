from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import requests, user_info, favorite, messages
from .form import TestForm, PostForm, StatusForm, DocumentForm, UserForm, EvaForm
from django.contrib.auth.decorators import login_required
from .models import Document

def index(request):
    posts = requests.objects.all().filter(matching_complete=False)
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
        my_dict['form'] = PostForm(request.POST, request.FILES)
        user = request.user
        post = requests(
            client_id=user,
            title=request.POST.get('title'),
            text=request.POST.get('text'),
            departure_place=request.POST.get('departure_place'),
            destination_place=request.POST.get('destination_place'),
            delivery_date=request.POST.get('delivery_date'),
            asking_price=request.POST.get('asking_price'),
            photo=request.FILES.get('photo'),
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
        user = request.user
        flag = False
        if request.POST.get('is_driver') == 'on':
            flag = True
        default_eval = 3.0
        post = user_info(
            user_name=user, 
            is_driver=flag,
            region=request.POST.get('region'),
            total_socore=default_eval,
        )
        post.save()
        return redirect('main:profile')
    return render(request, "main/profile.html", use_dict)

@login_required
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
        'status': chat_room,
    }
    if (request.method == "POST"):
        my_dict['form'] = TestForm(request.POST)
        user = request.user
        post_comment = messages(user_id=user, post_id = chat_room, text=request.POST.get('text', False))
        post_comment.save()
        return redirect('main:chat',  num=num)
    return render(request, 'main/chat.html', my_dict)

def message(request):
    return render(request, 'main/message.html')

@login_required
def payment(request, num):
    chat_room = requests.objects.get(id=num)
    my_dict = {
        'id': chat_room.id,
        'price': chat_room,
        'form': StatusForm,
    }
    if (request.method == "POST"):
        paystatus = requests.objects.get(id=num)
        paystatus.payment = True
        paystatus.save()
        print(paystatus.payment)
        return redirect('main:chat',  num=num)
    return render(request, "main/payment.html", my_dict)

@login_required
def log(request):
    user = request.user
    before_posts = requests.objects.all().filter(client_id=user, matching_complete=False)
    matching_posts = requests.objects.all().filter(client_id=user, matching_complete=True, request_complete=False)
    after_posts = requests.objects.all().filter(client_id=user, request_complete=True)
    favorites_posts = requests.objects.all().filter(request_complete=False) #お気に入り機能できたら修正
    all_posts = requests.objects.all().filter(client_id=user)
    header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
    my_dict = {
        'before_posts': before_posts,
        'matching_posts': matching_posts,
        'after_posts': after_posts,
        'favorites_posts': favorites_posts,
        'all_posts': all_posts,
        'header': header,
    }
    return render(request, 'main/log.html', my_dict)

# @login_required
# def log_before(request):
#     user = request.user
#     posts = requests.objects.all().filter(client_id=user, request_complete=False, matching_complete=False)
#     header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
#     my_dict = {
#         'posts': posts,
#         'header': header,
#     }
#     return render(request, 'main/log_before.html', my_dict)

# @login_required
# def history(request):
#     user = request.user
#     posts = requests.objects.all().filter(client_id=user, request_complete=False, matching_complete=True)
#     header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
#     my_dict = {
#         'posts': posts,
#         'header': header,
#     }
#     return render(request, 'main/history.html', my_dict)

# @login_required
# def match_complete(request):
#     user = request.user
#     header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
#     posts = requests.objects.all().filter(client_id=user, request_complete=True)
#     my_dict = {
#         'posts': posts,
#         'header': header,
#     }
#     return render(request, 'main/match_complete.html', my_dict)

# @login_required
# def favorites(request):
#     user = request.user
#     posts = requests.objects.all().filter(client_id=user, matching_complete=True)
#     header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
#     my_dict = {
#         'posts': posts,
#         'header': header,
#     }
#     return render(request, 'main/favorites.html', my_dict)

# @login_required
# def done_post(request):
#     user = request.user
#     posts = requests.objects.all().filter(client_id=user)
#     header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
#     my_dict = {
#         'posts': posts,
#         'header': header,
#     }
#     return render(request, 'main/done_post.html', my_dict)

@login_required
def detail(request, num):
    posts = requests.objects.all().filter(id=num)
    print(num)
    header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
    my_dict = {
        'id': num,
        'posts': posts,
        'header': header,
        'form': StatusForm,
    }
    if (request.method == "POST"):
        match = requests.objects.get(id=num)
        match.matching_complete = True
        match.save()
        return redirect('main:chat',  num=num)
    return render(request, 'main/detail.html', my_dict)

@login_required
def request_complete(request, num):
    posts = requests.objects.all().filter(id=num)
    print(num)
    header = ['ユーザー','タイトル','目的地','出発地','配達日時','詳細']
    my_dict = {
        'id': num,
        'posts': posts,
        'header': header,
        'form': StatusForm,
    }
    if (request.method == "POST"):
        match = requests.objects.get(id=num)
        match.request_complete = True
        match.save()
        return redirect('main:evaluation', num=num)
    return render(request, 'main/request_complete.html', my_dict)

@login_required
def evaluation(request, num):
    posts = requests.objects.all().filter(id=num)
    eva = requests.objects.get(id=num)
    user = request.user
    my_dict = {
        'id': num,
        'posts': posts,
        'form': EvaForm,
    }
    if (request.method == "POST"):
        return redirect('main:log')
    return render(request, 'main/evaluation.html', my_dict)
