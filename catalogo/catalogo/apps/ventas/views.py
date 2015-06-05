# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from catalogo.apps.ventas.forms import add_product_form, add_marca_form,add_categoria_form
from catalogo.apps.ventas.models import Producto, Marca, Categoria
from django.http import HttpResponseRedirect


def  add_product_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_product_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.status = True
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/producto/%s ' %add.id)
	else:
		formulario = add_product_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_producto.html', ctx,context_instance = RequestContext(request))

def  add_marca_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_marca_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/marcas' )
	else:
		formulario = add_marca_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_marca.html', ctx,context_instance = RequestContext(request))

def add_categoria_view(request):
	info = "inicializando"
	if request.method == "POST":
		formulario = add_categoria_form(request.POST,request.FILES)
		if formulario.is_valid():
			add = formulario.save(commit = False)
			add.save() #guarda la informacion
			formulario.save_m2m() #guarda las relaciones ManyToMany
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect ('/categorias')
	else:
		formulario = add_categoria_form()
	ctx ={ 'form':formulario,'informacion':info}
	return render_to_response('ventas/add_categoria.html', ctx,context_instance = RequestContext(request))

def edit_product_view(request, id_prod):
	info = ""
	prod = Producto.objects.get(pk = id_prod)
	if request.method == "POST":
		formulario = add_product_form(request.POST, request.FILES, instance = prod)
		if formulario.is_valid():
			edit_prod = formulario.save(commit = False )
			formulario.save_m2m()
			edit_prod.status = True
			edit_prod.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/producto/%s'% edit_prod.id)
	else:
		formulario = add_product_form(instance = prod)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_producto.html', ctx, context_instance = RequestContext(request))

def edit_marca_view(request, id_marca):
	info = ""
	marc = Marca.objects.get(pk = id_marca)
	if request.method == "POST":
		formulario = add_marca_form(request.POST, request.FILES, instance = marc)
		if formulario.is_valid():
			edit_marc = formulario.save(commit = False )
			formulario.save_m2m()
			edit_marc.status = True
			edit_marc.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/marcas')
	else:
		formulario = add_marca_form(instance = marc)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_marca.html', ctx, context_instance = RequestContext(request))

def edit_categoria_view(request, id_categ):
	info = ""
	categ = Categoria.objects.get(pk = id_categ)
	if request.method == "POST":
		formulario = add_categoria_form(request.POST, request.FILES, instance = categ)
		if formulario.is_valid():
			edit_categ = formulario.save(commit = False )
			formulario.save_m2m()
			edit_categ.status = True
			edit_categ.save()
			info = "Guardado Satisfactoriamente"
			return HttpResponseRedirect('/categorias')
	else:
		formulario = add_categoria_form(instance = categ)
	ctx = {'form': formulario, 'informacion':info}
	return render_to_response ('ventas/edit_categoria.html', ctx, context_instance = RequestContext(request))

def del_product_view(request,id_prod):
	info = "inicializando"
	try:
		prod = Producto.objects.get(pk = id_prod)
		prod.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect ('/productos/page/1')
	except:
		info = "Producto no se puede eliminar "
		return HttpResponseRedirect ('/productos/page/1')

def del_marca_view(request,id_marca):
	info = "inicializando"
	try:
		marc = Marca.objects.get(pk = id_marca)
		marc.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect ('/marcas')
	except:
		info = "Producto no se puede eliminar "
		return HttpResponseRedirect ('/marcas')

def del_categoria_view(request,id_categ):
	info = "inicializando"
	try:
		categ = Categoria.objects.get(pk = id_categ)
		categ.delete()
		info = "Producto Eliminado Correctamente"
		return HttpResponseRedirect ('/categorias')
	except:
		info = "Producto no se puede eliminar "
		return HttpResponseRedirect ('/categorias')
		

	





