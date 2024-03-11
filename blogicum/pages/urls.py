from django.urls import path
from .views import category, about, rules

app_name = 'pages'

urlpatterns = [
    path('about/', about, name = 'about'),
    path('category/', category, name = 'category'),
    path('rules/', rules, name = 'rules'),

]