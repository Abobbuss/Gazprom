from django.contrib import admin
from . import models

# Получить список всех имен моделей в модуле models
model_names = [name for name in dir(models) if isinstance(getattr(models, name), type)]

# Зарегистрировать каждую модель, кроме модели User, в административной панели
for model_name in model_names:
    model = getattr(models, model_name)
    if model_name != "User":
        admin.site.register(model)
