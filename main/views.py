from django.db.models import Q

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet, GenericViewSet

from likes.mixins import LikedMixin
from .models import Product, Comment, Favorite
from .permissions import IsProductAuthor
from .serializers import ProductSerializer, CommentSerializer, FavoriteSerializer


class ProductView(ModelViewSet, LikedMixin):
    permission_classes = [IsAuthenticated, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category',]

    @action(detail=False, methods=['get'])
    def search(self, request, pk=None):
        q = request.query_params.get('q')
        queryset = self.queryset
        queryset = queryset.filter(Q(title__icontains=q) |
                                   Q(description__icontains=q))
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsProductAuthor, ]
        else:
            permissions = []
        return [permission() for permission in permissions]


    def get_serializer_context(self):
        return {
            'request': self.request
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

class CommentView(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsProductAuthor, ]
        else:
            permissions = []
        return [permission() for permission in permissions]





# ------------------------------------------------------------------------------------------------------

class FavoriteView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'product'


    def get_serializer_context(self):
        return {'request': self.request}

    def get_object(self):
        obj, _ = Favorite.objects.get_or_create(user=self.request.user, product_id=self.kwargs['book'])
        return obj



















