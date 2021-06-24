from django.contrib import admin
from myapp.models import UserModel, CategoryModel

# Register your models here.

admin.site.register(UserModel)
admin.site.register(CategoryModel)
