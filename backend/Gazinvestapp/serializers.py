from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

    def validate_name(self, value):
        # Проверка на уникальность категории
        if models.Category.objects.filter(name=value).exists():
            raise serializers.ValidationError("Категория с таким именем уже существует.")
        return value

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'