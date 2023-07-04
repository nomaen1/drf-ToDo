from rest_framework import serializers
from apps.todo.models import ToDo
from apps.users.models import User

class ToDoSerializer(serializers.ModelSerializer):
    class Meta: 
        model = ToDo
        fields = "__all__"