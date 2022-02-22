from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('product', ProductView)
router.register('comment', CommentView)
router.register('favorite', FavoriteView)

urlpatterns = [
    path('', include(router.urls)),

]

