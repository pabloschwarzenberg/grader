class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.capacidad_estanque=capacidad_estanque
      self.nivel_estanque=0
      self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      self.velocidad=velocidad
      self.tiempo=tiempo
      distancia=self.velocidad*self.tiempo
      self.nivel_estanque-=(distancia//self.rendimiento)
    def autonomia(self):
      return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,litros):
      self.litros=litros
      if self.litros>self.capacidad_estanque:
        a=(self.capacidad_estanque-self.nivel_estanque)
        return (a,False)
      else:
        self.nivel_estanque=self.litros
        return (self.litros,True)
if __name__ == "__main__":
    auto=Auto(100,12)
         