class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        pass
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    def andar(self, velocidad, tiempo):
      x=velocidad*tiempo
      y=self.nivel_estanque*self.rendimiento
      posible=y-x
      if posible>=0:
        self.nivel_estanque=self.nivel_estanque-(x/self.rendimiento)
        return(0)
      else:
        self.nivel_estanque=0
        return(posible*-1)
    def autonomia(self):
      return(self.nivel_estanque*self.rendimiento)
    def llenar_estanque(self, litros):
      posible=self.capacidad_estanque-self.nivel_estanque
      cantidad=self.nivel_estanque+litros
      if cantidad>posible:
        return(posible, False)
      else:
        self.nivel_estanque=self.nivel_estanque+litros
        return(self.nivel_estanque, True)
        

if __name__ == "__main__":
    auto=Auto(100,12)
         