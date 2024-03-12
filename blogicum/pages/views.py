from django.shortcuts import render

# Create your views here.


def about(request):
    """О программе"""
    return render(request, 'pages/about.html')


def category(request):
    """Категория"""
    return render(request, 'pages/category.html')


def rules(request):
    """Правила"""
    return render(request, 'pages/rules.html')
