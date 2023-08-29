class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuenkilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      distancia=velocidad*tiempo
      litros=distancia/self.rendimiento
      if litros>self.nivel_estanque:
        norecorrido=distancia-(self.rendimiento*self.nivel_estanque)
        self.nivel_estanque=0
        self.kilometraje+=self.rendimiento*self.nivel_estanque
        self.cuenta_kilometros+=self.rendimiento*self.nivel_estanque
        return norecorrido
      else:
        self.nivel_estanque-=litros
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        return 0
    def autonomia(self):
      return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,litros):
      if self.capacidad_estanque<self.nivel_estanque+litros:
        return self.capacidad_estanque,False
      else:
        self.nivel_estanque+=litros
        return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)
         