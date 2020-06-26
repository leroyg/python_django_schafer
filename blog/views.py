from django.shortcuts import render

posts = [
    {
        'author': 'LeRoyG',
        'title': 'Blog Post',
        'content': 'First Post Content',
        'date_posted': 'June 26, 2020'
    },
    {
        'author': 'JackJ',
        'title': 'Blog Post Too',
        'content': '2nd Post Content',
        'date_posted': 'June 29, 2020'
    },
    {
        'author': 'SheenaE',
        'title': 'Blog Post Three',
        'content': '3rd Post Content',
        'date_posted': 'June 22, 2020'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
