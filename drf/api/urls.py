from django.urls import path, re_path, include

from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# Определение URL-шаблонов для API
urlpatterns = [
    
    # URL для отображения списка всех пользователей
    path('users-list/', views.UserList.as_view()),
    
    # URL для отображения деталей конкретного пользователя по его ID
    path('users-detail/<int:pk>/', views.UserDetail.as_view()),
    
    # URL для отображения списка всех постов и создания новых постов
    path('posts/', views.PostList.as_view()),
    
    # URL для отображения, обновления и удаления конкретного поста по его ID
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    
    # URL для отображения списка всех комментариев и создания новых комментариев
    path('comments/', views.CommentList.as_view()),
    
    # URL для отображения, обновления и удаления конкретного комментария по его ID
    path('comments/<int:pk>/', views.CommentDetail.as_view()),
    
    # URL для отображения списка всех категорий и создания новых категорий
    path('categories/', views.CategoryList.as_view()),
    
    # URL для отображения, обновления и удаления конкретной категории по её ID
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
]


accounts_urlpatterns = [
    re_path(r'^api/v1/', include('djoser.urls')),
    re_path(r'^api/v1/', include('djoser.urls.authtoken')),
]

# Применение format_suffix_patterns для поддержки различных форматов ответов (например, JSON, XML)
urlpatterns = format_suffix_patterns(urlpatterns)