from django.db import models

# Create your models here.

class Categoria(models.Model):
	nombre 			 = models.CharField(max_length = 100)
	descripcion		 = models.TextField(max_length = 500)

	def __unicode__ (self):
		return self.nombre

class Marca (models.Model):
	nombre 			 = models.CharField(max_length = 100)
	
	def __unicode__(self):
			return self.nombre

class Producto (models.Model):

	def url(self, filname):
			ruta = "MultimediaData/Producto/%s/%s"%(self.nombre, str(filname))
			return ruta


	nombre 			 = models.CharField(max_length = 100)
	descripcion		 = models.TextField(max_length = 500)
	status 			 = models.BooleanField(default = True)
	imagen 			 = models.ImageField(upload_to = url, null = True, blank = True)
	precio 			 = models.DecimalField(max_digits = 6, decimal_places = 2)
	stock 			 = models.IntegerField()
	categoria 		 = models.ManyToManyField(Categoria, null = True, blank = True)
	marca 			 = models.ForeignKey(Marca)

	def __unicode__ (self):
		return self.nombre