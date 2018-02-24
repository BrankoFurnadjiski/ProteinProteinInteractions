"""
	This class represents how strongly a protein is connected to a neighbour
"""
class ProteinWrapper:
	def __init__(self, neighbour, weight):
		self.__neighbour = neighbour
		self.__weight = weight

	def __str__(self):
		return '(%s: %d)' % (self.__neighbour, self.__weight)

	def getProtein(self):
		return self.__neighbour

	def getWeight(self):
		return self.__weight