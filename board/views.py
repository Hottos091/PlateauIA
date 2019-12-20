from django.shortcuts import render
from django.http import HttpResponse
from board.models import Board

def home(request):
	return HttpResponse("""
			<h1>IA VS. Human</h1>

		""")


def game(request, size):
	#Instanciation du plateau

	#On saisit le code ascii de la chaine de caractères qui forme la grille (le plateau)
	"""Conversion ascii -> html
	conv = Ansi2HTMLConverter()
	ansi = grid
	html = conv.convert(ansi)"""
	return render(request, 'board/test.html')
