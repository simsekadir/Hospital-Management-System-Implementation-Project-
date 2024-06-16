from django.contrib import admin
from django.urls import path, include
from base_project_py.views import home, system_page, appointment_list, appointment_create, prescription_list, prescription_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', home, name='home'),
    path('system/', system_page, name='system_page'),
    path('appointments/', appointment_list, name='appointment_list'),
    path('appointments/create/', appointment_create, name='appointment_create'),
    path('prescriptions/', prescription_list, name='prescription_list'),
    path('prescriptions/create/', prescription_create, name='prescription_create'),
]
