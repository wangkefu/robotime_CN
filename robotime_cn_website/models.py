from __future__ import unicode_literals

from django.db import models

class Group(models.Model):
    name=models.CharField(max_length=120)
    description=models.CharField(max_length=120)


    def __unicode__(self):
        return self.name

# Create your models here.
class Category(models.Model):
    group_id=models.ForeignKey(Group)
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    def __unicode__(self):
        return self.name

class RtProduct(models.Model):
    category_id=models.ForeignKey(Category,null=True)
    name = models.CharField(max_length=120)
    image = models.ImageField(blank=True,upload_to = 'update/%Y%m%d')
    # image_url = models.BinaryField(blank=True)

    def __unicode__(self):
        return self.name






