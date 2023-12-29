from rest_framework import serializers
from .models import Question

class Questionserializer(serializers.ModelSerializer):
     class Meta:
        model=Question
        field=('Question_txt','pub_date','exp_sol','answer')