from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def chat(request):
    return render(request, 'main/chat.html')