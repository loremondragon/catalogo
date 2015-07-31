from django.contrib import admin
from catalogo.apps.ventas.models import Marca, Producto, Categoria
from catalogo.apps.home.models import user_profile
admin.site.register(Marca)
admin.site.register(user_profile)
admin.site.register(Producto)
admin.site.register(Categoria)