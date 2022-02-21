from rest_framework import serializers

import likes

from .models import Product, Comment


class ProductSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['comments'] = CommentSerializer(instance.comments.all(), many=True).data


        return representation

    def get_is_fan(self, obj):

        user = self.context.get('request').user
        return likes.services.is_fan(obj, user)

    def create(self, validated_data):
        request = self.context.get('request')
        product = Product.objects.create(author=request.user, **validated_data)
        return product



class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Comment
        fields = "__all__"

    def create(self, validated_data):
        user = self.context.get('request').user
        comment = Comment.objects.create(
            author=user,
            **validated_data
        )
        return comment


