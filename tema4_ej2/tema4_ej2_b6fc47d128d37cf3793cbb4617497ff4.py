class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.capacidad_estanque=capacidad_estanque
      self.nivel_estanque=0
      self.rendimiento=rendimiento
    def cuenta_kilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      distancia=velocidad*tiempo
      litros=(self.rendimiento**(-1))*distancia
      self.kilometraje+=distancia
      self.cuenta_kilometros+=distancia
      if self.nivel_estanque>=litros:
        self.nivel_estanque-=litros
        return 0
      else:
        kilometros=distancia-(self.nivel_estanque*self.rendimiento)
        return kilometros
    def autonomia(self):
      return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,cantidad):
      if self.capacidad_estanque-self.nivel_estanque>=cantidad:
        self.nivel_estanque+=cantidad
        return self.nivel_estanque, True
      else:
        return self.capacidad_estanque-self.nivel_estanque, False
     

if __name__ == "__main__":
    auto=Auto(100,12)
         