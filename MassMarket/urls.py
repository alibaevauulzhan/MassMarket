from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MassMarket import settings
from MassMarket.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/v1/', include('main.urls')),
    # path('api/v1/', include('comment.urls')),
]+ static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
