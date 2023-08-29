import math
class Auto:
	def __init__(self,capacidad_estanque,rendimiento):
		self.kilometraje=0
		self.cuenta_kilometros=0
		self.capacidad_estanque=capacidad_estanque
		self.nivel_estanque=0              #menor o igual a capacidad_estanque
		self.rendimiento=rendimiento

	def reiniciar_cuentakilometros(self):
		self.cuenta_kilometros=0

	def autonomia(self):
		return self.rendimiento*self.nivel_estanque   #km/l * l


	def llenar_estanque(self,litros):
		if self.capacidad_estanque>=self.nivel_estanque+litros:
			self.nivel_estanque=self.nivel_estanque+litros
			return (self.nivel_estanque, True)
		else:
			return(litros+self.nivel_estanque, False)


	def andar(self,velocidad,tiempo):
		distancia=velocidad*tiempo
		if distancia<self.rendimiento*self.nivel_estanque:
			return 0
		else:
			return abs((distancia-self.rendimiento*self.nivel_estanque))

#Caso particular
if __name__ == "__main__":
	auto1=Auto(100,12)
	viaje=input("Cuanta distancia desea viajar? ")
	capacidad_viaje=rendimiento.auto1*nivel_estanque.auto1
	numero_detenciones=(viaje//capacidad_viaje)
