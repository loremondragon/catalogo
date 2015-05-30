from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('catalogo.apps.home.views', 
	url(r'^about/$','about_view', name = 'vista_about'),
	url(r'^contacto/$','contacto_view', name = 'vista_contacto'),
	url(r'^$','index_view', name = 'vista_index'),
	url(r'^marcas/$','marcas_view', name = 'vista_marcas'),
	url(r'^categorias/$','categorias_view', name = 'vista_categorias'),
	url(r'^producto/(?P<id_prod>.*)/$','single_product_view', name = 'vista_single_producto'),
	url(r'^productos/page/(?P<pagina>.*)/$', 'productos_view', name= 'vista_productos'),
	url(r'^login/$', 'login_view', name = 'vista_login'),
	url(r'^logout/$', 'logout_view', name = 'vista_logout'),
	url(r'^registro/$','register_view', name = 'vista_registro'),


)
