from django.shortcuts import redirect, render
from .models import request  # import追加
from .form import PostAdd

# Create your views here.
def create(request):
    message = ''
    if (request.method == 'POST'):
        form = PostAdd(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect(to='/index')
        else:
            message = "再入力してください"
    modelform_dict = {
        'title':'依頼投稿ページ',
        'form': PostAdd(),
        'message': message,
    }
    return render(request, 'post/create.html', modelform_dict)