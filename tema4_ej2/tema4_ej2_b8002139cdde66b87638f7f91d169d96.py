class Auto:
  def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
  def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
  def andar(self,velocidad,tiempo):
        self.kilometraje=self.kilometraje+int(velocidad*tiempo)
        self.cuenta_kilometros=self.cuenta_kilometros+int(velocidad*tiempo)
        self.nivel_estanque=self.nivel_estanque-((velocidad*tiempo)/self.rendimiento)
        if self.nivel_estanque>=0:
            return 0
        else:
          return ("Te falto por recorrer {0} kilometros").format(self.cuenta_kilometros-1200)         
  def autonomia(self):
      m=self.nivel_estanque*self.rendimiento
      return m
  def llenar_estanque(self,nuevoestanque):
      if self.nivel_estanque+nuevoestanque>self.capacidad_estanque:
          return (100,False)
      else:
          self.nivel_estanque=self.nivel_estanque+nuevoestanque
          return (self.nivel_estanque,True)
if __name__ == "__main__":
    auto=Auto(100,12)
         