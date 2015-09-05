from catalogo.apps.ventas.models import Producto,Marca,Categoria

from django import forms

class add_product_form(forms.ModelForm):
	class Meta:
		model = Producto
		#se excluye el status por que en el modelo lo ponemos default=True
		exclude = {'status',}

class add_marca_form(forms.ModelForm):
	class Meta:
		model = Marca
		#se excluye el status por que en el modelo lo ponemos default=True
				
class add_categoria_form(forms.ModelForm):
	class Meta:
		model = Categoria
		#se excluye el status por que en el modelo lo ponemos default=True
