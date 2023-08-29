class Auto:
    def __init__(self, capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
      pass
    
    def andar(self,velocidad,tiempo):
      self.nivel_estanque=self.nivel_estanque-(velocidad*tiempo)/self.rendimiento
      self.kilometraje=self.kilometraje+velocidad*tiempo
      self.cuenta_kilometros=self.cuenta_kilometros+velocidad*tiempo
      if self.nivel_estanque>=self.rendimiento*velocidad*tiempo:
        return 0
      else:
        falto=velocidad*tiempo-self.nivel_estanque*self.rendimiento
        return falto
     
    def autonomia(self):
      km=self.nivel_estanque*self.rendimiento
      return km
    
    def llenar_estanque(self,litros):
      if litros+self.nivel_estanque<=self.capacidad_estanque:
        self.nivel_estanque=self.nivel_estanque+litros
        return [self.nivel_estanque,True]
      else:
        return [self.capacidad_estanque,False]

if __name__ == "__main__":
    auto=Auto(100,12)