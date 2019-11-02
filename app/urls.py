from django.contrib import admin
from django.urls import path
from .core.views import index, faker_user, user_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faker/<id:int>', faker_user),
    path('v1/users', user_all),
    path('', index)
]
