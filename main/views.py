from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def top_share(request):
    return render(request, 'main/top_share.html')


def chat(request):
    return render(request, 'main/chat.html')