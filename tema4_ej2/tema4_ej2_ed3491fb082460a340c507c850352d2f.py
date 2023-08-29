class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque = capacidad_estanque
      self.rendimiento = rendimiento
      self.kilometraje = 0
      self.cuenta_kilometraje = 0
      self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometraje = 0
    
    def andar(self,velocidad,tiempoviaje):
      lauto = self.nivel_estanque * self.rendimiento
      lquiere = velocidad*tiempoviaje
      if lauto >= lquiere:
        self.kilometraje = self.kilometraje + lquiere
        self.cuenta_kilometros = lquiere
        self.nivel_estanque = self.nivel_estanque - lquiere/self.rendimiento
        return 0
      else:
        lfalta = lquiere-lauto
        self.kilometraje = self.kilometraje + lauto
        self.cuenta_kilometros = lauto
        self.nivel_estanque = self.nivel_estanque - lauto/self.rendimiento
        print("Aun le faltan {0} kilometros".format(lfalta))
        
    def autonomia(self):
      kilometros = self.nivel_estanque * self.rendimiento
      return kilometros
      
    def llenar_estanque(self,litros):
      if litros + self.nivel_estanque > self.capacidad_estanque:
        return (self.capacidad_estanque , False)
      else:
        self.nivel_estanque += litros
        return (self.nivel_estanque , True)
        


if __name__ == "__main__":
    auto=Auto(100,12)
    
         