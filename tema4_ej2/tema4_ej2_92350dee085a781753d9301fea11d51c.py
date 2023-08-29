class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.nivel_estanque=0
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
    def andar(self, velocidad, tiempo):
        self.cuenta_kilometros=velocidad*tiempo
        self.kilometraje=self.kilometraje+self.cuenta_kilometros
        self.nivel_estanque=self.capacidad_estanque-(self.cuenta_kilometros/self.rendimiento)
        if self.nivel_estanque>=0:
            return 0
        else:
            return "Faltan recorrer: "
    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros
    def llenar_estanque(self,litros):
        self.nivel_estanque=self.nivel_estanque+litros
        if self.nivel_estanque>self.capacidad_estanque:
            return self.capacidad_estanque-self.nivel_estanque,False

if __name__ == "__main__":
    auto=Auto(100,12)
         