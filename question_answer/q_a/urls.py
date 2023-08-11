from django.urls import path
from .views import HomeView, PythonView ,PythonansView,QA_form

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('python/', PythonView.as_view(), name='python'),
    path('form',QA_form,name='form'),
    path('python/<int:x_id>/',PythonansView.as_view(),name='pythonans')
]
