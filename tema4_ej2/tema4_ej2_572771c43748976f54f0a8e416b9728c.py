class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje = 0
      self.cuenta_kilometros = 0
      self.capacidad_estanque = capacidad_estanque
      self.nivel_estanque = 0
      self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros = 0
    def andar(self, vel, tiem):
      dist = vel*tiem
      kmrest = self.nivel_estanque*self.rendimiento
      tot = dist-kmrest
      print(dist,kmrest,tot)
      return 0
    def autonomia(self):
      return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self, litros):
      if litros+self.nivel_estanque > self.capacidad_estanque:
        return self.capacidad_estanque, False
      else:
        self.nivel_estanque += litros
        return self.nivel_estanque, True
if __name__ == "__main__":
    auto=Auto(100,12)
         