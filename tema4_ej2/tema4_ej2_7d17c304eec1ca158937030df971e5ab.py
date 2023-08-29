class Auto:
	
	def __init__(self, capacidad_estanque, rendimiento):
		
		self.kilometraje=0
		self.cuenta_kilometros=0
		self.capacidad_estanque=capacidad_estanque
		self.nivel_estanque=0
		self.rendimiento=rendimiento

	def reiniciar_cuentakilometros(self):
		
		self.cuenta_kilometros=0

	def andar(self, velocidad, tiempo):
		
		km=velocidad*tiempo
		litros_necesarios=km/self.rendimiento

		if litros_necesarios<=self.nivel_estanque:
			
			self.kilometraje+=km
			self.cuenta_kilometros+=km
			self.nivel_estanque-=litros_necesarios
			return 0
			
		else:
			
			intervalo=km-(self.nivel_estanque * self.rendimiento)
			self.kilometraje+=(self.nivel_estanque * self.rendimiento)
			self.cuenta_kilometros+=(self.nivel_estanque * self.rendimiento)
			self.nivel_estanque=0
			return intervalo

	def autonomia(self):
		
		return self.nivel_estanque*self.rendimiento

	def llenar_estanque(self, litros):
		
		if litros<=self.capacidad_estanque:
			
			self.nivel_estanque=litros
			return self.nivel_estanque, True
			
		else:
			
			return self.capacidad_estanque, False


if __name__=='__main__':
	
	auto=Auto(100, 12)

	viaje=[(80, 2), (60, 3), (70, 1), (90, 4)]

	paradas=0

	for velocidad, tiempo in viaje:
		
		intervalo=auto.andar(velocidad, tiempo)
		
		if intervalo>0:
			
			paradas+=1

	print("Numero de paradas necesarias: "+str(paradas))
         