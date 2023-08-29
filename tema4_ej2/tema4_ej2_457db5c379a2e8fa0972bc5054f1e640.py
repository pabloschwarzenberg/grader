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
      distancia=velocidad*tiempo
      gasto=distancia*self.rendimiento
      if gasto>self.nivel_estanque:
        distanciarecorrida=self.nivel_estanque*self.rendimiento
        return (distancia-distanciarecorrida)
      else:
        return 0
        
    def autonomia(self):
      puederecorrer=self.capacidad_estanque*self.rendimiento
      return puederecorrer
      
    def llenar_estanque(self,cantidad):
      self.nivel_estanque=self.nivel_estanque+cantidad
      if self.nivel_estanque>self.capacidad_estanque:
        tupla=(self.capacidad_estanque,False)
        return tupla
      else:
        tupla=(self.nivel_estanque,True)
        return tupla
      
    

if __name__ == "__main__":
    auto=Auto(100,12)
         