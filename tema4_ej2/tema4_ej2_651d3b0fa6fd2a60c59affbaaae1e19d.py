class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje=0
      self.cuenta_kilometraje=0
      self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
      #d=v*t
      if self.rendimiento*self.nivel_estanque>velocidad*tiempo:
        self.cuenta_kilometraje=velocidad*tiempo+self.cuenta_kilometraje
        self.kilometraje=velocidad*tiempo+self.kilometraje
        self.nivel_estanque =self.nivel_estanque- (velocidad*tiempo)/self.rendimiento
        return 0
      else:
        return (velocidad*tiempo-self.rendimiento*self.nivel_estanque)
    def autonomia(self):
      return (self.rendimiento*self.nivel_estanque)
    def llenar_estanque(self,llenado):
      if (self.capacidad_estanque-self.nivel_estanque)<llenado:
        return ((self.capacidad_estanque,False))
      else:
        self.nivel_estanque=self.nivel_estanque+llenado
        return ((self.nivel_estanque,True))

if __name__ == "__main__":
    auto=Auto(100,12)
         