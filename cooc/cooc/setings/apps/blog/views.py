from django.shortcuts import render
from django.views.generic import ListView

from .models import Post

from django.views.decorators.csrf import csrf_protect

# Create your views here.


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs.get("slug"))


def news(request):
    con_text = Post.objects.all()
    titl = Post.objects.all()

    context = {"text_list": con_text, "titl_list": titl}

    return render(request, "blog/new.html", context)

@csrf_protect

def home(request):
    return render(request, "blog/index.html")
