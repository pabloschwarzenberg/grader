class Ciudad:
	
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def camino(self, otra_ciudad):
		
		pasos=[]
		dx=(otra_ciudad.x )-self.x
		dy=(otra_ciudad.y)-self.y
		pasos2=max(abs(dx), abs(dy))

		for i in range(pasos2):
			
			x=self.x+int(round(dx* i / pasos2))
			y=self.y+int(round(dy* i / pasos2))
			pasos.append([x, y])

		pasos.append([otra_ciudad.x, otra_ciudad.y])
		
		return pasos

	def distancia(self, otra_ciudad):
		
		dx=(otra_ciudad.x)-self.x
		dy=(otra_ciudad.y)-self.y
		distancia=((dx**2)+(dy**2))**0.5
		return distancia


if __name__=='__main__':
	
	p1=Ciudad(1, 1)
	p2=Ciudad(3, 3)
	camino=p1.camino(p2)
	distancia=p1.distancia(p2)

	print("Pasos: ", camino)
	print("Distancia: ", distancia)