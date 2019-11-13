from django.db import models
from django.utils import timezone
from django.urls import reverse
import os
import datetime

from user_account.models import Account

# Create your models here.
def rename_path(path):
    def create_path(instance, filename):
        date_path = datetime.datetime.now()
        extension = filename.split('.')[-1]

        if instance.pk:
            filename = "{}.{}".format(instance.pk, extension)
        else:
            filename = "A-{}{}{}-{}{}{}.{}".format(date_path.year, date_path.month, date_path.day, date_path.hour, date_path.minute, date_path.second, extension)
        return os.path.join(path, filename)
    return create_path

class Announcement(models.Model):
    author = models.ForeignKey('user_account.Account', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    picture = models.ImageField(default='default.jpg', upload_to=rename_path('announcement_pics'))
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("announcement:announcement_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    


