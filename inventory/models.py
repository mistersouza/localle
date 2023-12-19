from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models

# Models
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    original_price = models.DecimalField(
        decimal_places=2, max_digits=10, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='inventory/', blank=True, null=True)
    on_sale = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    stars = models.IntegerField(default=0)
    created_by = models.ForeignKey(
        User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def clean(self):
        if self.stars < 0 or self.stars > 5:
            raise ValidationError('Stars must be between 0 and 5.')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
