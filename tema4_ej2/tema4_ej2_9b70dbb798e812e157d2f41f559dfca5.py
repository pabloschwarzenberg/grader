class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
      return self.cuenta_kilometros
    def andar(self,velocidad, tiempo):
      anda=int(velocidad*tiempo)
      litros=anda/self.rendimiento
      self.nivel_estanque=int(self.nivel_estanque-litros)
      self.kilometraje=int(self.kilometraje+anda)
      maxa=int(self.nivel_estanque*self.rendimiento)
      if maxa==anda:
        print("no puede seguir avanzando")
    def autonomia(self):
      autonomia=int(self.nivel_estanque*self.rendimiento)
      return autonomia
    def llenar_estanque(self,litros):
      self.nivel_estanque=(self.nivel_estanque+litros)
      if self.nivel_estanque>self.capacidad_estanque:
        return (self.capacidad_estanque, False)
      else:
         return (self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         