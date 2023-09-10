from django.db import models

NULLABLE = {'null': True, 'blank': True}

 
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='содержимое', **NULLABLE)
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    views = models.IntegerField(default=0, verbose_name='просмотры')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
