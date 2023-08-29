class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentaKilometraje(self):
      self.cuenta_kilometraje=0
      
    def andar(self,velocidad,tiempo_viaje):
      consumo=(velocidad*tiempo_viaje)/self.rendimiento
      distancia=velocidad*tiempo_viaje
      self.nivel_estanque-=consumo
      self.kilometraje+=distancia
      self.cuenta_kilometros+=distancia
      if consumo <= self.nivel_estanque:
        return 0
      else:
        return consumo-self.nivel_estanque
      
      
      
      
    def autonomia(self):
      return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,cantidad_litros):
      if self.nivel_estanque+cantidad_litros > capacidad_estanque:
        return [[self.capacidad_estanque],[False]]
      else:
        
        

if __name__ == "__main__":
    auto=Auto(100,12)
         