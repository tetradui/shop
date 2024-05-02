from django.db import models
from slugify import slugify

class Category(models.Model): 
    title = models.CharField(max_length=30, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=30, primary_key=True, blank=True)

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)


class Product(models.Model): 
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категории')
    title = models.CharField(max_length=50, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=50,primary_key=True, blank=True)
    image = models.ImageField(upload_to='products_img/', blank=True, verbose_name='Картинки')
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveBigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self): 
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)

class ProductImage(models.Model):
    image = models.ImageField(upload_to='products_img/')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')