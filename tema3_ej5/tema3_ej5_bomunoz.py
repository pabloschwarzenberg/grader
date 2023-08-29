
#3)
import math

class Ciudad:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __add__(coordenada1,coordenada2):
		coordenada3=Ciudad((coordenada1.x+coordenada2.x),(coordenada1.y+coordenada2.y))
		return coordenada3

	def __sub__(ciudad1,ciudad2):
		ciudad3=Ciudad(abs(ciudad1.x-ciudad2.x),abs(ciudad1.y-ciudad2.y))
		return ciudad3

	def __repr__(self):
		return "["+str(self.x)+","+str(self.y)+"]"        #Entrega el output en caso de presentarse un print

#def distancia(ciudad1,ciudad2):
#	return ((ciudad1.x-ciudad2.x)**2+(ciudad1.y-ciudad2.y)**2)**(1/2)
#
#def camino(ciudad1,ciudad2):
#	distancia1=distancia(ciudad1,ciudad2)
#	distancia_lateral=abs(ciudad1.x-ciudad2.x)             # No quiero definir las funciones al interior 
#	distancia_vertical=abs(ciudad1.y-ciudad2.y)
#
#	paso_lateral=distancia_lateral/distancia1
#	paso_vertical=distancia_vertical/distancia1
#	#partir del p.i, e ir agregando a la lista, pi+ paso latera+ paso vertical
#
#	#### revisar esto ######
#	pasox=Ciudad(ciudad1.x,ciudad1.y)
#	contador=0
#	lista_pasos=[]
#	while int(distancia1)+1>contador:
#		lista_pasos.append(pasox)
#		pasox=pasox+Ciudad(paso_lateral,paso_vertical)
#		contador=contador+1
#	print (lista_pasos)

	def distancia(self,ciudad2):
		return ((self.x-ciudad2.x)**2+(self.y-ciudad2.y)**2)**(1/2)

	def camino(self,ciudad2):
		distancia1=distancia(self,ciudad2)
		distancia_lateral=abs(self.x-ciudad2.x)             # No quiero definir las funciones al interior 
		distancia_vertical=abs(self.y-ciudad2.y)

		paso_lateral=distancia_lateral/distancia1
		paso_vertical=distancia_vertical/distancia1
		#partir del p.i, e ir agregando a la lista, pi+ paso latera+ paso vertical

		#### revisar esto ######
		pasox=Ciudad(self.x,self.y)
		contador=0
		lista_pasos=[]
		while int(distancia1)+1>contador:
			lista_pasos.append(pasox)
			pasox=pasox+Ciudad(paso_lateral,paso_vertical)
			contador=contador+1
		return (lista_pasos)