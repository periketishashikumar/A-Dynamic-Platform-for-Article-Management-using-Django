from django.shortcuts import render
from django.db.models import Q
from .models import Article
# Create your views here.
def index(request):
    rows = Article.objects.all()
    if request.method == "POST":
        search = request.POST.get('search') 
        rows = Article.objects.filter(Q(title__icontains = search) | Q (description__icontains = search))
        # print(search1)
    return render(request,'index.html',{'data' : rows})
def article(request,id):
    row = Article.objects.get(id=id)
    return render(request,'article.html',{'data':row})
def nav(request):
    return render(request,'nav.html')
