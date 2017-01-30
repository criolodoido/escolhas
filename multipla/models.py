from django.db import models

class Classificacao(models.Model):
	TIPOS = (
		('COMIDA', 'Alimentacao'),
		('EDUCA', 'Educacao'),
		('ACESS', 'Acessorios'),
		('HIGI', 'Higienizacao'),
		('ANTI', 'Antiparazitas'),
	)
	name = models.CharField(max_length=100)
	tipos = models.CharField(max_length=6, choices=TIPOS)

	def publish(self):
		self.save()

	def __str__(self):
		return self.tipos