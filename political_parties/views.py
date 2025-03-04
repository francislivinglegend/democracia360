from django.shortcuts import get_object_or_404, redirect, render

from utils.forms import RegistrationForm
from .models import Political_Party
from django.contrib.auth.forms import *
from django.contrib.auth import authenticate, login

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    political_parties_list = Political_Party.objects.all()
    context = {
        "political_parties_list": political_parties_list,
    }
    return render(request, "political_parties/index.html", context)

def detail(request, question_id):
    political_party = get_object_or_404(Political_Party, pk=question_id)
    return render(request, "political_parties/detail.html", {"political_party": political_party})