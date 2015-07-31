# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_product_form
from catalogo.apps.ventas.models import Producto 
from django.http import HttpResponseRedirect

def add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save()
			formulario.save_m2m()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s'%add.id)
	else:
		formulario = add_product_form()
	ctx = {'form':formulario,'informacion':info}
	return render_to_response('ventas/add_product.html', ctx,context_instance = RequestContext(request))

def del_product_view(request, id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect('/productos/')
	except:
		info = "Producto no se puede eliminar"	
		return HttpResponseRedirect('/productos/')
		