from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user,name='logout'),
    path('register/', views.register_user,name='register_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('change_password/', views.change_password,name='change_password'),
    path('view_staff/', views.show_users,name='view_staff'),




    path('laptop_entry/', views.laptop_entry,name='laptop_entry'),
    path('desktop_entry/', views.desktop_entry,name='desktop_entry'),
    path('recovery_entry/', views.recovery_entry,name='recovery_entry'),


    path('input_laptop_entry/', views.input_laptop_entry,name='input_laptop_entry'),
    path('input_desktop_entry/', views.input_desktop_entry,name='input_desktop_entry'),
    path('input_recovery_entry/', views.input_recovery_entry,name='input_recovery_entry'),

    # path('inquery/', include('inquery.urls')),
    
    path('components/', views.home1,name='home1'),
    path('orders/', views.home1,name='home1'),


    path('desktop_entry/<int:entry_id>',  views.delete_desktop_entry, name='delete_desktop_entry'),
    path('laptop_entry/<int:entry_id>',  views.delete_laptop_entry, name='delete_laptop_entry'),
    path('recovery_entry/<int:entry_id>',  views.delete_recovery_entry, name='delete_recovery_entry'),


    path('desktop_entry/<int:entry_id>/', views.update_desktop_entrybook, name='update_desktop_entrybook'),
    path('laptop_entry/<int:entry_id>/', views.update_laptop_entrybook, name='update_laptop_entrybook'),
    path('recovery_entry/<int:entry_id>/', views.update_recovery_entrybook, name='update_recovery_entrybook'),







]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

