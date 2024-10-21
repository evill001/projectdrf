from django.db import models

# Модель для представления поста
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания поста (автоматически устанавливается при создании)
    title = models.CharField(max_length=100, blank=True, default='')  # Заголовок поста (максимум 100 символов, может быть пустым)
    body = models.TextField(blank=True, default='')  # Тело поста (текст, может быть пустым)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)  # Владелец поста (связь с моделью User, при удалении пользователя удаляются все его посты)

    class Meta:
        verbose_name_plural = 'посты'
        verbose_name = 'пост'
        ordering = ['created']  # Сортировка постов по дате создания (от старых к новым)

    def __str__(self):
        return self.title
# Модель для представления комментария
class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментария (автоматически устанавливается при создании)
    body = models.TextField(blank=False)  # Тело комментария (текст, не может быть пустым)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)  # Владелец комментария (связь с моделью User, при удалении пользователя удаляются все его комментарии)
    post = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)  # Пост, к которому относится комментарий (связь с моделью Post, при удалении поста удаляются все его комментарии)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name_plural = 'комментарии'
        verbose_name = 'комментарий'
        ordering = ['created']  # Сортировка комментариев по дате создания (от старых к новым)

# Модель для представления категории
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')  # Название категории (максимум 100 символов, не может быть пустым)
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)  # Владелец категории (связь с моделью User, при удалении пользователя удаляются все его категории)
    posts = models.ManyToManyField('Post', related_name='categories', blank=True)  # Посты, относящиеся к этой категории (многие-ко-многим связь с моделью Post, может быть пустым)

    class Meta:
        verbose_name_plural = 'категории'
        verbose_name = 'категория'
        verbose_name_plural = 'categories'  # Устанавливает правильное множественное число для названия модели в админке (чтобы не было "Categorys")

    def __str__(self):
        return self.name