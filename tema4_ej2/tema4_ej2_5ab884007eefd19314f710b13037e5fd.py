class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.capacidad_estanque=capacidad_estanque
      self.nivel_estanque=0
      self.rendimiento=rendimiento
    
    def llenar_estanque(self,litros):
      llenar=self.nivel_estanque+litros
      if llenar<=self.capacidad_estanque:
        self.nivel_estanque=llenar
        return (llenar,True)
      elif llenar>self.capacidad_estanque:
        return (self.capacidad_estanque,False)

    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
      return
    
    def andar(self,velocidad,tiempo):
      distancia=velocidad*tiempo
      self.kilometraje=self.kilometraje+distancia
      self.cuenta_kilometros=self.cuenta_kilometros+distancia
      distancia_maxima=self.nivel_estanque*self.rendimiento
      if distancia_maxima<distancia:
        self.nivel_estanque=0
        falta=distancia-distancia_maxima
        return falta
      elif distancia_maxima>=distancia:
        gasto=distancia/self.rendimiento
        self.nivel_estanque=self.nivel_estanque-gasto
        return 0
    def autonomia(self):
      distancia=self.nivel_estanque*self.rendimiento
      return distancia

if __name__ == "__main__":
    auto=Auto(100,12)
         