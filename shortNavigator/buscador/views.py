from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.shortcuts import render

from .models import Word, Paper

def index(request):
  template = loader.get_template('buscador/index.html')
  return HttpResponse(template.render(request=request))

def results(request, word):
  try:
    indices = Word.objects.filter(word=word)
    articulos = sorted([Paper.objects.get(pk=i.origin.pk) for i in indices], 
                       key=lambda o: o.rank, reverse=True)
    if len(articulos) > 10:
      articulos = articulos[:10]
  except Word.DoesNotExist:
    raise Http404('Palabra no encontrada')
  response = 'Resultados con la palabra %s'
  return render(request,'buscador/results.html',
                {'papers':articulos})

def see_paper(request, id):
  print(id)
  try:
    paper = Paper.objects.get(paper_id=id)
    paper.authors = paper.authors[2:-3].replace('\'','').replace(',',', ')
  except Paper.DoesNotExist:
    raise Http404('Identificador falso')
  return render(request, 'buscador/show_paper.html',
                {'paper':paper})