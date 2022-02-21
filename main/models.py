from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from MassMarket import settings
from likes.models import Like


from django.db import models

class CreatedAtModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class Product(CreatedAtModel):
    CATEGORY = [
        ('electronics', 'electronics'),
        ('home', 'home'),
        ('clothing', 'clothing'),
        ('beauty', 'beauty'),
        ('health', 'health'),
    ]
    category = models.CharField(max_length=20,choices=CATEGORY)
    title = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    author = models.ForeignKey('account.User', on_delete=models.CASCADE, related_name='problems'
    )
    body = models.CharField(max_length=140)
    likes = GenericRelation(Like)


    def __str__(self):
        return self.body

    @property
    def total_likes(self):
        return self.likes.count()




class Comment(CreatedAtModel):
    comment = models.TextField()
    author = models.ForeignKey('account.User', related_name='comments', on_delete=models.CASCADE)
    product = models.ForeignKey('Product', related_name='comments',on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.comment


