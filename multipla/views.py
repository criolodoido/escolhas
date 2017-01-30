from django.shortcuts import render
from django.utils import timezone
from .models import Classificacao

def home(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/home.html', {'posts': posts})

#todos os outros defs, depois de home, foram modificados

def comida(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/comida.html', {'posts': posts})

def higiene(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/higiene.html', {'posts': posts})

def acessorios(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/acessorios.html', {'posts': posts})

def anti(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/anti.html', {'posts': posts})

def educa(request):
	posts = Classificacao.objects.all()
	return render(request, 'multipla/educa.html', {'posts': posts})