class Ciudad:
	
	def __init__(self, a, b):
		self.a=a
		self.b=b

	def camino(self, sentido):
		
		pasos=[]
		DistanciaA=(sentido.a )-self.a
		DistanciaB=(sentido.b)-self.b
		pasos2=max(abs(DistanciaA), abs(DistanciaB))

		for i in range(pasos2):
			
			a=self.a+int(round(DistanciaA* i / pasos2))
			b=self.b+int(round(DistanciaB* i / pasos2))
			pasos.append([a, b])

		pasos.append([sentido.a, sentido.b])
		
		return pasos

	def distancia(self, sentido):
		
		DistanciaA=(sentido.a)-self.a
		DistanciaB=(sentido.b)-self.b
		distancia=((DistanciaA**2)+(DistanciaB**2))**0.5
		return distancia


if __name__=='__main__':
	
	p1=ciudad(1, 1)
	p2=ciudad(3, 3)
	camino=p1.camino(p2)
	distancia=p1.distancia(p2)

	print("Pasos: ", camino)
	print("Distancia: ", distancia)