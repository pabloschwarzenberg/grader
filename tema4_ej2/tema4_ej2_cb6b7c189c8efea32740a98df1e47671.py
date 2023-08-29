class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuentakilometros=0
      self.capacidad_estanque=float(capacidad_estanque)
      self.nivel_estanque=0
      self.rendimiento=float(rendimiento)
    def reiniciar_cuentakilometros(self):
      self.cuentakilometros=0
    
    def andar(self,velocidad,tiempo):
      v=float(velocidad)
      t=float(tiempo)
      kilometros_max=self.nivel_estanque*self.rendimiento
      kilometros=v*t
      if kilometros_max >= kilometros:
        self.nivel_estanque -= kilometros/self.rendimiento
        self.kilometraje += kilometros
        self.cuentakilometros += kilometros
        return 0
      else:
        self.nivel_estanque -= kilometros_max/self.rendimiento
        self.kilometraje += kilometros_max
        self.cuenta_kilometros += kilometros_max
        distancia=kilometros-kilometros_max
        return distancia
        
    def autonomia(self): 
      kilometros_max=self.nivel_estanque*self.rendimiento
      return kilometros_max
    
    def llenar_estanque(self,litros):
      if float(litros)>self.capacidad_estanque-self.nivel_estanque:
        return self.capacidad_estanque-self.nivel_estanque,False
      else:
        self.nivel_estanque += float(litros)
        return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)
         