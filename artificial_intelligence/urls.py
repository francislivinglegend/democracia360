from django.urls import path
from . import views

app_name = 'artificial_intelligence'

urlpatterns = [
    # ex: /artificial_intelligence/
    path("", views.index, name="index"),
]