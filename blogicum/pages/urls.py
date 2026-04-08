from django.urls import path

from .views import about, rules

app_name = 'pages'

urlpatterns = [
    path('pages/about/', about, name='about'),
    path('pages/rules/', rules, name='rules'),
]
