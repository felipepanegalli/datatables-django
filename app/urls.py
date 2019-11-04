from django.contrib import admin
from django.urls import path
from .core.views import index, faker_user, user_all, datatables

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faker/<int:id>', faker_user),
    path('v1/users', user_all),
    path('', index),
    path('datatables/', datatables),
]
