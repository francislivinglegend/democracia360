from django.shortcuts import render
from django import forms
from google import genai
import os

# Create your views here.
def index(request):
    form = QueryForm()
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = QueryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=form.cleaned_data['query']
            )
            context = {
                'query': form.cleaned_data['query'],
                'response': response.text,
                'form': form,
            }

    # if a GET (or any other method) we'll create a blank form
    else:
        context = {
            'form': form,
        }
    return render(request, "artificial_intelligence/index.html", context)



class QueryForm(forms.Form):
    query = forms.CharField(label="Your query", max_length=100)