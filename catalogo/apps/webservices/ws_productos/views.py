# Create your views here.
from django.http import HttpResponse
from catalogo.apps.ventas.models import Producto
from django.core import serializers 
from catalogo.apps.ventas.models import *
from .serializer import producto_serializer,marca_serializer,categoria_serializer
from rest_framework import viewsets

def ws_productos_view(request,tipo):
	tipoF = tipo.lower()
	if tipoF=="json":
		mime= "application/json"
	elif tipoF == "xml":
		mime= "application/xml"
	 

	data = serializers.serialize(tipoF,Producto.objects.filter(status = True))
	return HttpResponse(data,mimetype=mime)


class producto_viewset(viewsets.ModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = producto_serializer
class marca_viewset(viewsets.ModelViewSet):
	queryset = Marca.objects.all()
	serializer_class = marca_serializer
class categoria_viewset(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = categoria_serializer