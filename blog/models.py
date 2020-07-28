from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from taggit.managers import TaggableManager

from user.models import Profile


class Category(MPTTModel):
    name = models.CharField('Название', max_length=40)
    slug = models.SlugField('Url', max_length=45, unique=True)
    description = models.TextField('Описание', max_length=300)
    parent = TreeForeignKey(
        'self',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_slug', args=[str(self.slug)])


class Post(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Url', max_length=55, unique=True)
    description = models.TextField('Описание', max_length=300)
    text = models.TextField('Текст')
    category = models.ForeignKey(
        Category,
        related_name='Category',
        on_delete=models.CASCADE,
    )
    tag = TaggableManager(blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Последние обновление', auto_now=True)
    to_display = models.BooleanField('Показать?', default=False)
    for_auth = models.BooleanField('Для авторизованных пользователей?', default=False)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_slug', args=[str(self.slug)])


class Product(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField('Название', max_length=50)
    slug = models.SlugField('Url', max_length=55, unique=True)
    description = models.TextField('Описание', max_length=300)
    post = models.ForeignKey(
        Post,
        related_name='Post',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    tag = TaggableManager(blank=True)
    created_date = models.DateTimeField('Дата создания', auto_now_add=True)
    update_date = models.DateTimeField('Последние обновление', auto_now=True)
    to_display = models.BooleanField('Показать?', default=False)
    for_auth = models.BooleanField('Для авторизованных пользователей?', default=False)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_slug', args=[str(self.slug)])


