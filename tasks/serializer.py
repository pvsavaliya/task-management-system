from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    assignees = UserSerializer(many=True, read_only=True)
    assignee_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), write_only=True, source='assignees')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'owner', 'assignees', 'assignee_ids', 'created_at', 'updated_at']

    def create(self, validated_data):
        assignees_data = validated_data.pop('assignees', [])
        task = Task.objects.create(**validated_data)
        task.assignees.set(assignees_data)
        return task

    def update(self, instance, validated_data):
        assignees_data = validated_data.pop('assignees', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        instance.assignees.set(assignees_data)
        return instance


# User Registration Serializer
class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
