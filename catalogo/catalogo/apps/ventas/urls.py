from django.conf.urls.defaults import patterns, url

urlpatterns = patterns ('catalogo.apps.ventas.views',
		url (r'^add/producto/$','add_product_view',name = 'vista_agregar_producto'),
		url (r'^edit/producto/(?P<id_prod>.*)/$','edit_product_view', name = 'vista_editar_producto'),
		url (r'^del/producto/(?P<id_prod>.*)/$', 'del_product_view', name = 'vista_eliminar_producto'),
		url (r'^add/marca/$','add_marca_view',name = 'vista_agregar_marca'),
		url (r'^add/categoria/$','add_categoria_view',name = 'vista_agregar_categoria'),
		url (r'^edit/marca/(?P<id_marca>.*)/$','edit_marca_view', name = 'vista_editar_marca'),
		url (r'^del/marca/(?P<id_marca>.*)/$', 'del_marca_view', name = 'vista_eliminar_marca'),
		url (r'^edit/categoria/(?P<id_categ>.*)/$','edit_categoria_view', name = 'vista_editar_categoria'),
		url (r'^del/categoria/(?P<id_categ>.*)/$', 'del_categoria_view', name = 'vista_eliminar_categoria'),
	)