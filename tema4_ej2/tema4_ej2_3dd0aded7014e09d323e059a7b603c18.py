class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje=0
      self.nivel_estanque=0
      self.cuenta_kilometros=0
      
    def llenar_estanque(self,litros):
      cantidad_litros=self.nivel_estanque + litros
      if cantidad_litros <= self.capacidad_estanque:
        self.nivel_estanque = cantidad_litros
        return (cantidad_litros,True)
      else:
        return(self.capacidad_estanque,False)
      
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometro=0
      
    def andar(self,velocidad,tiempo):
      distancia=tiempo*velocidad
      self.kilometraje += distancia
      self.cuenta_kilometros += distancia
      distancia_max = self.nivel_estanque*self.rendimiento
      if distancia_max < distancia:
        no_llego=distancia-distancia_max
        return no_llego
      else:
        costo=distancia/self.rendimiento
        self.nivel_estanque -= costo
        return 0
        
    def autonomia(self):
      distancia_maxima = self.nivel_estanque*self.rendimiento
      return distancia_maxima

if __name__ == "__main__":
    auto=Auto(100,12)
         