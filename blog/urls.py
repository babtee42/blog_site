from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('index/', views.index, name='index'),  # Example route for the blog app
    path('hello/', views.hello, name="hello"),
]