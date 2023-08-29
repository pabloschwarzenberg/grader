class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.capacidad_estanque=capacidad_estanque
      self.nivel_estanque=0
      self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
      
    def andar(self,velocidad,tiempo_viaje):
      self.kilometraje=self.kilometraje+(tiempo_viaje*velocidad)
      self.cuenta_kilometros=self.cuenta_kilometros+tiempo_viaje*velocidad
      self.nivel_estanque=self.nivel_estanque-((tiempo_viaje*velocidad)/self.rendimiento)
      if self.nivel_estanque >= 0:
        return 0
      else: 
        return -(self.nivel_estanque)*(self.rendimiento)
      
    def autonomia(self):
      kilometros=self.rendimiento*self.nivel_estanque
      return kilometros
      
    def llenar_estanque(self,litros):
      if litros > self.capacidad_estanque-self.nivel_estanque:
        return (self.capacidad_estanque-self.nivel_estanque,False)
      elif litros > 0 and self.capacidad_estanque-self.nivel_estanque > litros:
        self.nivel_estanque=self.nivel_estanque+litros
        return (self.nivel_estanque,True)