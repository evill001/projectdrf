---
# Руководство программиста: Работа с Django REST Framework

---
## Введение

Данное руководство создано для разработчиков, работающих с API на базе Django и Django REST Framework. Оно охватывает ключевые аспекты:

- Использование классов `generics`.
- Управление правами доступа (`permissions`).
- Тестирование API с помощью **Postman**.

Это структурированный источник знаний, который поможет вам быстро освоить инструменты для разработки RESTful API.

---
## Содержание

1. [Схема базы данных](#схема-базы-данных)
2. [Работа с классами `generics`](#работа-с-классами-generics)
3. [Назначение прав доступа (`permissions`)](#назначение-прав-доступа-permissions)
4. [Заключение](#заключение)

---
## Схема базы данных

![Схема базы данных](./db_schema.jpg)

### Основные таблицы

- **User**: таблица пользователей.
- **Post**: таблица постов.
- **Comment**: таблица комментариев.
- **Category**: таблица категорий.

### Связи между таблицами

- **Post** связан с **User** через поле `owner` (один ко многим).
- **Comment** связан с **User** через поле `owner` (один ко многим).
- **Comment** связан с **Post** через поле `post` (один ко многим).
- **Category** связан с **User** через поле `owner` (один ко многим).
- **Category** связан с **Post** через поле `posts` (многие ко многим).

---
## Работа с классами `generics`

Django REST Framework предоставляет мощные классы `generics`, которые значительно упрощают создание CRUD-представлений. Вот несколько примеров их использования:

### Примеры классов `generics`

```python
from rest_framework import generics
from .models import Post, Comment, Category
from .serializers import PostSerializer, CommentSerializer, CategorySerializer

# Список всех постов и создание нового поста
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Отображение, обновление и удаление конкретного поста
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# Список всех комментариев и создание нового комментария
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Отображение, обновление и удаление конкретного комментария
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# Список всех категорий и создание новой категории
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Отображение, обновление и удаление конкретной категории
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
```

### Описание классов

- **`ListCreateAPIView`**: отображение списка объектов и создание новых.
- **`RetrieveUpdateDestroyAPIView`**: работа с конкретным объектом (чтение, обновление, удаление).

---
## Назначение прав доступа (`permissions`)

Права доступа в Django REST Framework управляют действиями пользователей с объектами. Вы можете использовать встроенные разрешения или создавать свои собственные.

### Пример создания разрешений

```python
from rest_framework import permissions

# Разрешение только для владельца объекта
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешение на чтение для всех
        if request.method in permissions.SAFE_METHODS:
            return True
        # Изменение разрешено только владельцу объекта
        return obj.owner == request.user

# Применение разрешений в представлении
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
```

### Описание встроенных разрешений

- **`IsAuthenticatedOrReadOnly`**: изменения доступны только аутентифицированным пользователям, для остальных разрешено чтение.
- **`IsOwnerOrReadOnly`**: доступ к редактированию объекта только у его владельца.

---
## Заключение

В данном руководстве представлены ключевые подходы к работе с Django REST Framework:

- Использование классов `generics` для быстрого создания API.
- Настройка разрешений для контроля доступа.
- Тестирование API с помощью **Postman** для обеспечения его функциональности.

Следуя этим инструкциям, вы сможете легко разрабатывать и поддерживать RESTful API для своих проектов.

