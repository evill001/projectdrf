# Руководство программиста

## Введение

Это руководство предназначено для разработчиков, которые будут работать с API, созданным с использованием Django и Django REST Framework. В руководстве описаны основные аспекты работы с классами `generics`, управление правами доступа (`permissions`), а также инструкции по тестированию API с использованием Postman.

## Содержание

1. [Схема базы данных](#схема-базы-данных)
2. [Работа с классами `generics`](#работа-с-классами-generics)
3. [Назначение прав доступа (`permissions`)](#назначение-прав-доступа-permissions)
4. [Работа в Postman](#работа-в-postman)

## Схема базы данных

![Схема базы данных](./db_schema.jpg)

### Таблицы:
- **User**: Таблица пользователей.
- **Post**: Таблица постов.
- **Comment**: Таблица комментариев.
- **Category**: Таблица категорий.

### Связи:
- **Post** связан с **User** через поле `owner` (один ко многим).
- **Comment** связан с **User** через поле `owner` (один ко многим).
- **Comment** связан с **Post** через поле `post` (один ко многим).
- **Category** связан с **User** через поле `owner` (один ко многим).
- **Category** связан с **Post** через поле `posts` (многие ко многим).

## Работа с классами `generics`

Django REST Framework предоставляет классы `generics`, которые упрощают создание представлений (views) для CRUD-операций. Вот примеры использования:

### Примеры классов `generics`:

```python
from rest_framework import generics
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

# Представление для списка всех постов и создания нового поста
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Представление для отображения, обновления и удаления конкретного поста
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Представление для списка всех комментариев и создания нового комментария
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Представление для отображения, обновления и удаления конкретного комментария
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Представление для списка всех категорий и создания новой категории
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Представление для отображения, обновления и удаления конкретной категории
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```

### Описание:
- **ListCreateAPIView**: Используется для отображения списка объектов и создания новых объектов.
- **RetrieveUpdateDestroyAPIView**: Используется для отображения, обновления и удаления конкретного объекта.

## Назначение прав доступа (`permissions`)

Права доступа управляют тем, кто может выполнять определенные действия с объектами. В Django REST Framework есть несколько встроенных разрешений, а также возможность создавать собственные.

### Примеры разрешений:

```python
from rest_framework import permissions

# Разрешение, которое позволяет только владельцу объекта его редактировать или удалять
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user

# Применение разрешений в представлениях
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
```

### Описание:
- **IsAuthenticatedOrReadOnly**: Разрешает доступ только аутентифицированным пользователям для изменения данных, а всем остальным – только чтение.
- **IsOwnerOrReadOnly**: Разрешает доступ к объекту только его владельцу для изменения или удаления.

## Работа в Postman

Postman – это инструмент для тестирования API. Вот как можно использовать Postman для работы с вашим API:

### 1. Установка и настройка Postman
- Скачайте и установите Postman с [официального сайта](https://www.postman.com/downloads/).
- Создайте новый рабочий профиль и настройте окружение для вашего API.

### 2. Тестирование API

#### Получение списка постов
- **Метод**: GET
- **URL**: `http://localhost:8000/posts/`
- **Описание**: Получение списка всех постов.

#### Создание нового поста
- **Метод**: POST
- **URL**: `http://localhost:8000/posts/`
- **Тело запроса**:
  ```json
  {
      "title": "Пост",
      "body": "Тело поста"
  }
  ```
- **Описание**: Создание нового поста.

#### Получение конкретного поста
- **Метод**: GET
- **URL**: `http://localhost:8000/posts/<id>/`
- **Описание**: Получение информации о конкретном посте по его ID.

#### Обновление поста
- **Метод**: PUT
- **URL**: `http://localhost:8000/posts/<id>/`
- **Тело запроса**:
  ```json
  {
      "title": "Обновленный пост",
      "body": "Обновленное тело поста"
  }
  ```
- **Описание**: Обновление информации о конкретном посте по его ID.

#### Удаление поста
- **Метод**: DELETE
- **URL**: `http://localhost:8000/posts/<id>/`
- **Описание**: Удаление конкретного поста по его ID.

### 3. Аутентификация
- Если ваше API требует аутентификации, используйте вкладку `Authorization` в Postman для настройки токена или базовой аутентификации.
![Создание токена](./postman-create-token.png)

### 4. Тестирование других ресурсов
- Аналогично тестируйте другие ресурсы, такие как комментарии и категории, используя соответствующие URL и методы.

## Заключение

Это руководство предоставляет основные инструкции по работе с API, созданным с использованием Django и Django REST Framework. Используя классы `generics` и правильно настроенные разрешения, вы можете легко управлять доступом к вашим ресурсам. Postman поможет вам тестировать и отлаживать ваше API.
