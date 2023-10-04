from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(blank=True, null=True, verbose_name='описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='название')
    description = models.TextField(null=True, blank=True, verbose_name='описание')
    preview = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена за покупку')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    mod_date = models.DateTimeField(auto_now=True, verbose_name='дата изменения')

    def __str__(self):
        return f'{self.name} {self.category} {self.price} '

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


