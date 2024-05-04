from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from src.settings import MEDIA_URL, MEDIA_ROOT
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vlog.urls'))
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)