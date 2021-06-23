from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Status(models.Model):
    title = models.CharField(max_length=50, default="В обработке...")


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now())
    title = models.CharField(max_length=50)
    result = models.CharField(max_length=20, null=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    video = models.FileField(upload_to='media/videos/', null=True, blank=True)
    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def delete(self, using=None, keep_parents=False):
        self.video.delete()
        super().delete()

    class Meta:
        verbose_name = "Объект"
        verbose_name_plural = "Объекты"
