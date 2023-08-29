class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
        
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros = 0
      return self.cuenta_kilometros
      
    def andar(self,velocidad,tiempo):
      distancia = velocidad * tiempo
      litros = (distancia / self.rendimiento)
      kilometros_recorridos = (distancia - (self.nivel_estanque*self.rendimiento))
      self.kilometraje = self.kilometraje + distancia
      self.cuenta_kilometros = distancia
      if self.nivel_estanque - litros > 0:
        return 0
      else:
        return kilometros_recorridos
     
    
   
      
    def llenar_estanque(self,litros):  
      self.nivel_estanque = self.nivel_estanque + litros
      if self.nivel_estanque <= self.capacidad_estanque:
        return [self.nivel_estanque,True]
      else:
        return ["maximo litros",self.capacidad_estanque,False]
        
    def autonomia(self):
        aut = ( self.rendimiento * self.nivel_estanque)
        return aut
        
if __name__ == "__main__":
    auto=Auto(100,12)
        
      
      
      
      
    
   
 