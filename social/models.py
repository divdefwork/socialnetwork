from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Post(models.Model):
    """ Модель допису """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")
    body = models.TextField(verbose_name="Повідомлення")
    created_on = models.DateTimeField(default=timezone.now,
                                      verbose_name="Дата створення")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True,
                                      related_name='dislikes')

    objects = models.Manager()

    class Meta:
        """ Метадані моделі """
        verbose_name = 'Допис'
        verbose_name_plural = 'Дописи'

    def __str__(self):
        return self.body[:30]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               verbose_name="Автор")
    post = models.ForeignKey('Post', on_delete=models.CASCADE,
                             verbose_name="Допис")
    comment = models.TextField(verbose_name="Коментар")
    created_on = models.DateTimeField(default=timezone.now,
                                      verbose_name="Дата створення")

    objects = models.Manager()

    class Meta:
        """ Метадані моделі """
        verbose_name = "Коментар"
        verbose_name_plural = "Коментарі"


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile',
                                on_delete=models.CASCADE,
                                verbose_name="Користувач")
    name = models.CharField(max_length=30, blank=True, null=True,
                            verbose_name="Ім'я")
    bio = models.TextField(max_length=500, blank=True, null=True,
                           verbose_name="")
    birth_date = models.DateField(null=True, blank=True,
                                  verbose_name="День народження")
    location = models.CharField(max_length=100, blank=True, null=True,
                                verbose_name="Розташування")
    picture = models.ImageField(upload_to='uploads/profile_pictures',
                                default='uploads/profile_pictures/default.png',
                                blank=True, verbose_name="Зображення")
    followers = models.ManyToManyField(User, blank=True,
                                       related_name='followers',
                                       verbose_name="Підписники")

    objects = models.Manager()

    class Meta:
        """ Метадані моделі """
        verbose_name = "Профіль користувача"
        verbose_name_plural = "Профілі користувачів"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
