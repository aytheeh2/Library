from django.db import models

# Create your models here.


class book(models.Model):
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    pdf = models.FileField(upload_to='books/pdf')
    cover = models.FileField(upload_to='books/cover', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural='Books'