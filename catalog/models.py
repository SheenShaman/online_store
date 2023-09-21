from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='картинки', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за единицу')
    date_of_creation = models.DateTimeField(verbose_name='дата создания', **NULLABLE)
    date_of_change = models.DateTimeField(verbose_name='дата изменения', **NULLABLE)

    def __str__(self):
        return f'{self.name}: {self.description}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='продукт')

    numbers_of_version = models.IntegerField(verbose_name='номер версии')
    name_of_version = models.CharField(max_length=100, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активная версия')

    def __str__(self):
        return f'{self.product}({self.numbers_of_version}) - {self.name_of_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
