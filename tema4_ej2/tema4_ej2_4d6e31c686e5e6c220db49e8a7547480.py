class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      if velocidad*tiempo<=self.nivel_estanque*self.rendimiento:
        self.nivel_estanque-=(velocidad*tiempo/self.rendimiento)
        return 0
      if velocidad*tiempo>self.nivel_estanque*self.rendimiento:
        return velocidad*tiempo-(self.nivel_estanque*self.rendimiento)
    def autonomia(self):
      k=self.nivel_estanque*self.rendimiento
      return k
    def llenar_estanque(self,litros):
      if litros<=self.capacidad_estanque-self.nivel_estanque:
        self.nivel_estanque+=litros
        return (litros+self.nivel_estanque, True)
      else:
        return (self.capacidad_estanque, False)
if __name__ == "__main__":
    auto=Auto(100,12)