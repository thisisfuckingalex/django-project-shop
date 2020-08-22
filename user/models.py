from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField('Имя', max_length=100, blank=True)
    last_name = models.CharField('Фамилия', max_length=100, blank=True)
    address = models.CharField('Адрес', max_length=300, blank=True)
    slug = models.SlugField('id', max_length=100000, unique=True)
    created_date = models.DateTimeField('Дата создание аккаунта', auto_now_add=True)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user, )
        super(Profile, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile', kwargs={'pk_profile': int(self.id)})

    def __str__(self):
        return self.slug

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()








