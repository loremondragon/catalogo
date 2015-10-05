from django.conf.urls.defaults import patterns, url 
#import settings

urlpatterns = patterns('catalogo.apps.ventas.views',
		url(r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		url(r'^del/producto/(?P<id_prod>.*)/$','del_product_view',name = 'vista_eliminar_producto'),

	)