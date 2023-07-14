from django.urls import path
from .views import HomeView, PythonView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('python/', PythonView.as_view(), name='python'),
]
