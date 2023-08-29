class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
        self.cuenta_kilometros=0
        self.kilometraje=0
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      if velocidad*tiempo<=self.nivel_estanque*self.rendimiento:
       self.kilometraje=self.kilometraje+velocidad*tiempo
       self.cuenta_kilometros=self.cuenta_kilometros+velocidad*tiempo
       self.nivel_estanque=self.nivel_estanque-velocidad*tiempo/self.rendimiento
       return 0
      else:
        self.kilometraje=self.kilometraje+self.autonomia
        self.cuenta_kilometros=self.cuenta_kilometros+self.autonomia
        self.nivel_estanque=0
        return velocidad*tiempo-self.autonomia
    def autonomia(self):
      Distancia=self.nivel_estanque*self.rendimiento
      return Distancia
    def llenar_estanque(self,litros):
      if litros>self.capacidad-self.nivel_estanque:
        return (self.capacidad,False)
      else:
        self.nivel_estanque=self.nivel_estanque+litros
        return (self.nivel_estanque,True)
if __name__ == "__main__":
    auto=Auto(100,12)
         