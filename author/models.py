from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse

from user.models import Profile


class Author(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)
    slug = models.SlugField('id', max_length=100000, unique=True)
    bio = models.TextField(max_length=500, blank=True)
    to_display = models.BooleanField('Принята заявку или нет', default=False)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user, )
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk_author': self.pk})

    def __str__(self):
        return self.slug
