from django.db.models.base import ModelStateFieldsCacheDescriptor
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import driver_requests, requests, user_info, favorite, messages, matchdriver
from .form import TestForm, PostForm, StatusForm, DocumentForm, UserForm, EvaForm
from django.contrib.auth.decorators import login_required
from .models import Document
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    posts = requests.objects.all().filter(matching_complete=False)
    regional_posts = {
        'posts': posts,
    }
    return render(request, 'main/index.html', regional_posts)


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
        return redirect('main:log')
    return render(request, 'main/post.html')


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
def chat(request, num):
    chat_room = requests.objects.get(id=num)
    comment = messages.objects.all().filter(post_id=chat_room.id)
    header = ['????????????','??????']
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
    favorites_posts = requests.objects.all().filter(request_complete=False) #???????????????????????????????????????
    all_posts = requests.objects.all().filter(client_id=user)
    # ???????????????????????????User_info
    login = user_info.objects.get(user_name=user)
    header = ['????????????','????????????', '?????????','?????????','????????????','??????']
    if (login.is_driver == True): # ?????????????????????
        match_log = matchdriver.objects.all().filter(driver_id=user)
        print(user)
        print(match_log)
        for list in match_log:
            log_all = requests.objects.get(id=list.id)   
            print(log_all)     
            driver_requests(
                md_id=user,
                title = log_all.title,
                matching_complete = log_all.matching_complete,
                request_complete = log_all.request_complete,
                payment = log_all.payment,
                share_or_not = log_all.share_or_not,
                post_time = log_all.post_time,
                text = log_all.text,
                departure_place = log_all.departure_place,
                destination_place = log_all.destination_place,
                delivery_date = log_all.delivery_date,
                asking_price = log_all.asking_price,
                driver_evaluation = log_all.driver_evaluation,
                client_evaluation = log_all.client_evaluation,
                photo = log_all.photo,
            ).save()
        dr = driver_requests.objects.filter(md_id=user).values('title', 'matching_complete', 'request_complete', 'payment', 'text', 'departure_place', 'destination_place', 'delivery_date', 'asking_price').distinct()
        print(dr)
        matching_posts = dr.all().filter(md_id=user, matching_complete=True, request_complete=False)
        after_posts = dr.all().filter(md_id=user, request_complete=True)
        header.pop(0)
    my_dict = {
        'before_posts': before_posts,
        'matching_posts': matching_posts,
        'after_posts': after_posts,
        'favorites_posts': favorites_posts,
        'all_posts': all_posts,
        'header': header,
        'login': login,
    }
    return render(request, 'main/log.html', my_dict)


@login_required
def detail(request, num):
    posts = requests.objects.all().filter(id=num)
    print(num)
    header = ['????????????','????????????','?????????','?????????','????????????','??????']
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
        user = request.user
        matchdriver(
            post_id = num,
            driver_id = user
        ).save()
        return redirect('main:chat',  num=num)
    return render(request, 'main/detail.html', my_dict)

@login_required
def request_complete(request, num):
    posts = requests.objects.all().filter(id=num)
    print(num)
    header = ['????????????','????????????','?????????','?????????','????????????','??????']
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
    my_dict = {
        'id': num,
        'posts': posts,
        'form': EvaForm,
    }
    # ????????????User_info
    c = requests.objects.get(id=num)
    c_user = user_info.objects.get(user_name=c.client_id)
    print(c_user)
    # ??????????????????User_info
    d = matchdriver.objects.get(post_id=num)
    d_user = user_info.objects.get(user_name=d.driver_id)
    # ???????????????????????????User _info
    user = request.user
    login = user_info.objects.get(user_name=user)
    if (request.method == "POST"):
        if (login.is_driver == False): #??????????????????????????????????????????
            casenumber = float(d_user.total_number) + float(1)
            d_user.total_number = casenumber
            total = d_user.total_socore
            d_user.total_socore = (float(request.POST.get('eva')) + float(total)) / float(d_user.total_number)
            print(d_user.total_socore)
            d_user.save()
        else:
            casenumber = float(d_user.total_number) + float(1)
            c_user.total_number = casenumber
            total = c_user.total_socore
            c_user.total_socore = (float(request.POST.get('eva')) + float(total)) / float(c_user.total_number)
            c_user.save()
        return redirect('main:log')
    return render(request, 'main/evaluation.html', my_dict)

@login_required
def update(request, num):
    post = requests.objects.get(id=num)
    form = PostForm(initial={
        'title': post.title,
        'text': post.text,
        'departure_place': post.departure_place,
        'destination_place': post.destination_place,
        'delivery_date': post.delivery_date,
        'asking_price': post.asking_price,
        'photo': post.photo,
    })
    update_dict = {
        'form': form,
        'post': post,
        'id': num,
    }
    if (request.method == "POST"):
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.departure_place = request.POST.get('departure_place')
        post.destination_place = request.POST.get('destination_place')
        post.delivery_date = request.POST.get('delivery_date')
        post.asking_price = request.POST.get('asking_price')
        post.photo = request.FILES.get('photo')
        post.save()
        return redirect('main:log')
    return render(request, 'main/update.html', update_dict)

@login_required
def delete(request, num):
    header = ['????????????','????????????','?????????','?????????','????????????','??????']
    message = ''
    post = requests.objects.get(id=num)
    if (request.method == 'POST'):
        post.delete()
        return redirect('main:log')
    delete_dict = {
        'header': header,
        'id': num,
        'post': post,
        'message': message,
    }
    return render(request, 'main/delete.html', delete_dict)