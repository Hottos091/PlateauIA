from django import template
from ..models import Board


register = template.Library()




@register.filter
def testest(value):
	board = Board.objects.get(id=1)
	output = board.move(1, value)

	board = output[0]

	outputString = output[1] + "POST MODEL : Pos 1 : " + str(board.pos1) + " Pos 2 : " + str(board.pos2)

	return outputString
@register.simple_tag
def testest1():
	return "Test1 : SUCCESS";


def updateBoard(upToDateBoard):
	board = upToDateBoard;
