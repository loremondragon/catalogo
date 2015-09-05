# Create your views here.
from django.http import HttpResponse
from catalogo.apps.ventas.models import Producto
from django.core import serializers


def ws_productos_view(request):
	data = serializers.serialize("xml",Producto.objects.filter(status = True))
	return HttpResponse(data, mimetype='application/xml')