from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    return redirect(reverse('political_parties:index'))
