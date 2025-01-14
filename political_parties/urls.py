from django.urls import path
from . import views

app_name = 'political_parties'


urlpatterns = [
    # ex: /political_parties/
    path("", views.index, name="index"),
    # ex: /political_parties/5/
    path("<int:question_id>/", views.detail, name="detail"),
]