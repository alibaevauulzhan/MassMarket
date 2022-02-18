from django.db import models
from django.db.models import Choices


class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class Product(CreatedAtModel):
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    author = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='problems'
    )

    def __str__(self):
        return f"{self.title} -> Author: {self.author.email}"