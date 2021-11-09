from django.urls.conf import path, include
from .views import home

urlpatterns = [
    path('', home, name="home"),
]
