from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  

    path('inquery/', views.show_inquery,name='inquery'),
    path('new_inquery/', views.submit_inquery,name='submit_inquery'),







]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)