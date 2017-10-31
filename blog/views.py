from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from .models import Article,Category
def hello(request):
    template = get_template('hello.html')

    html = template.render(locals())
    return HttpResponse(html)
def homepage(requeset):
    template = get_template('index.html')
    article = Article.objects.all()

    html = template.render(locals())
    return HttpResponse(html)