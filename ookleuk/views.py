from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'august 27th 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'august 28th 2018'
    }
]


#Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'ookleuk/home.html', context)

def about(request):
    return render(request, 'ookleuk/about.html', {'title': 'About'})

