from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(default='抖音:脑瘫聚集地', max_length=50)
    intro = models.CharField(default='这里写介绍', max_length=50)
    url = models.CharField(default='Http://', max_length=50)
    icon = models.ImageField(default='default_icon.png', upload_to='images/')
    image = models.ImageField(default='default_image.png', upload_to='images/')

    votes = models.IntegerField(default=1)
    pub_date = models.DateField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title