from django.urls import path
from .views import HomeView, PythonView ,PythonansView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('python/', PythonView.as_view(), name='python'),
    path('python/<int:x_id>/',PythonansView.as_view(),name='pythonans')
]
