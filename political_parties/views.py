from django.shortcuts import get_object_or_404, render
from .models import Political_Party


def index(request):
    political_parties_list = Political_Party.objects.all()
    context = {
        "political_parties_list": political_parties_list,
    }
    return render(request, "political_parties/index.html", context)

def detail(request, question_id):
    political_party = get_object_or_404(Political_Party, pk=question_id)
    return render(request, "political_parties/detail.html", {"political_party": political_party})