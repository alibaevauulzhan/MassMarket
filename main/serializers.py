from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Product
        exclude = ('created_at',)

    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #
    #
    #     return representation

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(author=request.user, **validated_data)
        return product
