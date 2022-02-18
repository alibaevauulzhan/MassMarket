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


class Comment(CreatedAtModel):
    comment = models.TextField()
    author = models.ForeignKey('account.User', related_name='comments', on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product', related_name='comments',on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.comment
