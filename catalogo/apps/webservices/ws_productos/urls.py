from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('catalogo.apps.webservices.ws_productos.views',
		url(r'^ws/productos/$','ws_productos_view',name = 'ws_productos_url'),
	)