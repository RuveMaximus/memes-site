from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime


User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор поста')
    text = models.CharField('Текст поста', max_length=255)
    likes = models.IntegerField('Лайки', default=0)
    dislikes = models.IntegerField('Дизлайки', default=0)
    pub_date = models.DateField('Дата публикации')
    image = models.ImageField('Изображение')

    def save(self, *args, **kwargs):
        self.author = User.objects.get(pk=1)
        self.pub_date = datetime.now()

        super(Post, self).save(*args, **kwargs)

    def __str__(self): 
        return f'Пост №{self.pk} от {self.author}'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    text = models.CharField('Текст', max_length=255)