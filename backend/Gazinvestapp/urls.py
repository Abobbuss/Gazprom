from . import views
from django.urls import path, include

urlpatterns = [
    path('',
        include([
             path('categories/', views.CategoryListCreateView.as_view(), name='category-list-create'),
             path('questions/', views.QuestionListCreateView.as_view(), name='question-list-create'),
             path('authenticate/', views.authenticate_user, name='authenticate_user'),
        ]))
]
