class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
     self.kilometraje=0
     self.cuenta_kilometros=0
     self.capacidad_estanque=100
     self.nivel_estanque=0
     self.rendimiento=12
     
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
      cuenta_kilometros=0 
     
    def andar(self,velocidad,t_viaje):
      distancia=velocidad*t_viaje
      distancia_ideal=self.nivel_estanque*self.rendimiento
      if distancia>distancia_ideal:
        self.nivel_estanque=0
        self.cuenta_kilometros=distancia_ideal
        self.kilometraje=self.kilometraje+distancia_ideal
        return distancia-distancia_ideal
      else:
        self.nivel_estanque=(distancia_ideal-distancia)/self.rendimiento
        self.cuenta_kilometros=distancia
        self.kilometraje=self.kilometraje+distancia
        
        return 0
 
    def autonomia(self):
      return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,cantidad_de_litros):
      if cantidad_de_litros+self.nivel_estanque>self.capacidad_estanque:
        return self.nivel_estanque-self.capacidad_estanque,False
      else:
        self.nivel_estanque= cantidad_de_litros+self.nivel_estanque       
        return self.nivel_estanque,True
        
      
      

if __name__ == "__main__":
    auto=Auto(100,12)
         