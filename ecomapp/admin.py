from django.contrib import admin
from .models import *

admin.site.register([Category,Customer,Cart,CartProduct,Order,Product,Admin])
