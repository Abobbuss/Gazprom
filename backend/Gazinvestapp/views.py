from rest_framework import generics
from . import models, serializers
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class QuestionListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.QuestionSerializer

    def get_queryset(self):
        # Получаем значение параметра запроса "category_id"
        category_id = self.request.query_params.get('category_id')
        
        # Фильтруем вопросы по категории, если параметр задан
        if category_id:
            return models.Question.objects.filter(category_id=category_id)
        
        # В противном случае, возвращаем все вопросы
        return models.Question.objects.all()

def authenticate_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Authentication successful'})
        else:
            return JsonResponse({'message': 'Authentication failed'}, status=401)

    return JsonResponse({'message': 'Invalid request method'}, status=400)
