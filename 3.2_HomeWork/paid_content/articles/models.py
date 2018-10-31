from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')
    text = models.TextField(verbose_name='Обзор')
    is_paid = models.BooleanField(verbose_name='Платная статья')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_subscription = models.BooleanField(verbose_name='Наличие подписки')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


