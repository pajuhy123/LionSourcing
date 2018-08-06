from django.db import models

# Create your models here.
class Main(models.Model):
    before_sentences = models.CharField(max_length=250)
    direct_links = models.CharField(max_length=150)

    def __str__(self):
        return self.before_sentences