from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^comida$', views.comida, name='comida'),
	url(r'^acessorios$', views.acessorios, name='acessorios'),
	url(r'^higiene$', views.higiene, name='higiene'),
	url(r'^anti$', views.anti, name='anti'),
	url(r'^educa$', views.educa, name='educa'),
]

