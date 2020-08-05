from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from pytils.translit import slugify
from django.urls import reverse

# from order.models import Order


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField('id', max_length=100000, unique=True)
    bio = models.TextField(max_length=500, blank=True)


    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user, )
        super(Author, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('profile_detail', args=[str(self.slug)])

    def __str__(self):
        return self.slug

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Author.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
