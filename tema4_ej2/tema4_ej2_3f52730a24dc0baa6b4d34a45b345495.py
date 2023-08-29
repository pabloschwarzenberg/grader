class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.nivel_estanque=0
    
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
    
    def autonomia(self):
      kilometros=self.rendimiento*self.nivel_estanque
      return kilometros
      
    def llenar_estanque(self,cant_litros):
      A=self.nivel_estanque+cant_litros
      if A>self.capacidad_estanque:
        tupla=(self.capacidad_estanque-self.nivel_estanque,False)
        return (tupla)
      else:
        self.nivel_estanque=A
        tupla2=(self.nivel_estanque,True)
        return (tupla2)
    
    def andar(self,velocidad,tiempo):
      viaje_km=10000
      distancia_rec=velocidad*tiempo
      litros_gastados=distancia_rec/self.rendimiento
      self.nivel_estanque=self.nivel_estanque-litros_gastados
      self.kilometraje=self.kilometraje+distancia_rec
      self.cuenta_kilometros=self.cuenta_kilometros+distancia_rec
      if self.cuenta_kilometros>=viaje_km:
        return 0
      else:
        return (viaje_km-self.cuenta_kilometros)
        
      

if __name__ == "__main__":
    auto=Auto(100,12)
         