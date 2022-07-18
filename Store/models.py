from django.db import models
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50,db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    @staticmethod
    def get_all_categories():
        return Category.objects.all()
        

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, default = '',blank = True, null = True)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/products/%Y')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_product(id):
        return Product.objects.get(id = id)

    @staticmethod
    # here ids is list of product id
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        img = Image.open(self.image.path)
        if img.height > 200 or img.width > 200:
            output_size = (150,150)
            # resize previous image
            img.thumbnail(output_size)
            # override previous image
            img.save(self.image.path)

