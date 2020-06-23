
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', include('entrybook.urls')),
    path('inquery/', include('inquery.urls')),
    path('components/', include('components.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
