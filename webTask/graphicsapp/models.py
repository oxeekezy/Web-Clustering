from django.db import models


class Vessels(models.Model):
    method = models.CharField('Method', max_length=3)
    cluster = models.IntegerField('Cluster')
    x = models.IntegerField('X')
    y = models.IntegerField('Y')

    def __str__(self):
        return self.x

