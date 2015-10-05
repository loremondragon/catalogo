# Create your views here.
from catalogo.apps.home.forms import contact_form
from catalogo.apps.home.forms import Login_form,RegisterForm

from catalogo.apps.ventas.models import Producto
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator,EmptyPage,InvalidPage


def register_view(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			usuario = form.cleaned_data['username']
			email = form.cleaned_data['email']
			password_one = form.cleaned_data['password_one']
			password_two = form.cleaned_data['password_two']
			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save()
			return render_to_response('home/thanks_register.html',context_instance = RequestContext(request) )
		else:
			ctx = {'form':form}	
			return render_to_response('home/register.html',ctx,context_instance = RequestContext(request) )
	ctx = {'form':form}	
	return render_to_response('home/register.html',ctx,context_instance = RequestContext(request) )	

def principal_view(request):
	return render_to_response('home/index.html',context_instance = RequestContext(request) )

def login_view(request):
	mensaje = ""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method == "POST":
			formulario = Login_form(request.POST)
			if formulario.is_valid():
				usu = formulario.cleaned_data['usuario']
				pas = formulario.cleaned_data['clave']
				usuario = authenticate(username = usu,password = pas)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje = "Usuario y/o clave incorrecta"
	formulario = Login_form()
	ctx = {'form':formulario,'mensaje':mensaje}
	return render_to_response('home/login.html',ctx,context_instance = RequestContext(request))

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')
	
def about_view(request):
	return render_to_response('home/about.html',context_instance = RequestContext(request) )

'''def contacto_view (request):
	formulario = contact_form()
	ctx = {'form':formulario}
	return render_to_response('home/contacto.html',ctx,context_instance = RequestContext(request))
'''
def contacto_view(request):
	info_enviado = False
	email = ""
	title = ""
	text = ""
	if request.method == "POST":
		formulario = contact_form(request.POST)
		if formulario.is_valid():
			info_enviado = True
			email = formulario.cleaned_data['correo']
			title = formulario.cleaned_data['titulo']
			text = formulario.cleaned_data['texto']
			'''Bloque configuracion de envio po GMAIL '''
			to_admin = 'hfportilla9@misena.edu.co'
			html_content = "informacion recibida de %s <br> ---mensaje--- <br> %s"%(email,text)
			msg = EmailMultiAlternatives('correo de contacto', html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content, 'text/html')
			msg.send()
			'''Fin del Bloque'''

	else:
		formulario = contact_form()
	ctx = {'form' :formulario, 'email' :email, 'title' :title, 'text' :text, "info_enviado":info_enviado}	
	return render_to_response('home/contacto.html',ctx, context_instance = RequestContext(request))

def  single_product_view(request, id_prod):
	prod = Producto.objects.get(id = id_prod)
	ctx = {'producto':prod}
	return render_to_response('home/single_producto.html',ctx,context_instance = RequestContext(request))

def productos_view(request,pagina):
	lista_prod= Producto.objects.filter(status = True)
	# SELECT * FROM Producto WHERE nombre LIKE '%silla'
	'''lista_prod = Producto.objects.filter(nombre__istartswith='silla')
				# SELECT * FROM Producto WHERE stock BETWEEN 3 AND 12
				lista_prod = Producto.objects.filter(stock__range=(0,1300))
				# SELECT * FROM Producto WHERE stock<13
				lista_prod = Producto.objects.filter(stock__lt=13)
				#SELECT * FROM Producto ORDER BY stock
				lista_prod = Producto.objects.order_by('stock')
				#SELECT nombre FROM Producto
				lista_prod = Producto.objects.values('nombre')
				#SELECT * FROM Producto WHERE stock>13
				lista_prod = Producto.objects.filter(stock__gt=13)
				#SELECT * FROM Producto WHERE NOT (nombre='silla')
				lista_prod = Producto.objects.exclude(nombre='bbq')
				# SELECT * FROM Producto WHERE stock<=13
				lista_prod = Producto.objects.filter(stock__lte=13)
				#SELECT * FROM Producto ORDER BY stock DESC LIMIT 1
				lista_prod = Producto.objects.order_by('stock').last()
				#SELECT * FROM Producto WHERE stock>=13
				lista_prod = Producto.objects.filter(stock__gte=13)
			'''

	paginator = Paginator(lista_prod,3)
	print paginator.num_pages
	try:
		page = int(pagina)
	except:
		page = 1
	try:
		productos = paginator.page(page)
	except (EmptyPage,InvalidPage):
		productos = paginator.page(paginator.num_pages)

	ctx = {'productos':productos}
	return render_to_response('home/productos.html',ctx,context_instance = RequestContext(request))