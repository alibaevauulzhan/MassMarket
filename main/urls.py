from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('product', ProductView)
# router.register('reply', ReplyViewSet)


urlpatterns = [
    path('', include(router.urls))

]