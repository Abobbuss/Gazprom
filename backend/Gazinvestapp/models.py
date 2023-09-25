from django.db import models
from django.contrib.auth.models import User  # Импорт модели пользователя Django

class Administrator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Связь с моделью пользователя Django
    role = models.CharField(max_length=255)  # Роль администратора

    def __str__(self) -> str:
        return self.user.first_name

class Category(models.Model):
    name = models.CharField(max_length=255)  # Название категории помощи

    def __str__(self) -> str:
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)  # Связь с моделью категорий помощи, разрешая значение пустым
    question = models.CharField(max_length=255)  # Текст вопроса
    answer = models.TextField()  # Текст ответа или HTML-код

    def __str__(self) -> str:
        return self.question

