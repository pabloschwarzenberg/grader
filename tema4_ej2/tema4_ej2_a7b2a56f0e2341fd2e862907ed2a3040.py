class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
       self.kilometraje=0
       self.cuenta_kilometros=0
       self.capacidad_estanque=capacidad_estanque
       self.nivel_estanque=0
       self.rendimiento=rendimiento
       
    def reiniciar_cuentakilometros(self):
      if self.cuenta_kilometros!=0:
         self.cuenta_kilometros=self.cuenta_kilometros-self.cuenta_kilometros
      else:
        self.cuenta_kilometros=self.cuenta_kilometros
    
    def andar(self,velocidad,tiempo_de_viaje):
       self.cuenta_kilometros=velocidad*tiempo_de_viaje
       self.kilometraje=velocidad*tiempo_de_viaje
       x=self.nivel_estanque-((velocidad*tiempo_de_viaje)/self.rendimiento)
       y=self.nivel_estanque
       if x<0:
         self.cuenta_kilometros=(velocidad*tiempo_de_viaje)-((velocidad*tiempo_de_viaje)-(y*self.rendimiento))
         self.kilometraje=(velocidad*tiempo_de_viaje)-((velocidad*tiempo_de_viaje)-(y*self.rendimiento))
         self.nivel_estanque=0
         return (velocidad*tiempo_de_viaje)-(y*self.rendimiento)
        
       else:
          self.cuenta_kilometros=velocidad*tiempo_de_viaje
          self.kilometraje=velocidad*tiempo_de_viaje
          self.nivel_estanque=self.nivel_estanque-((velocidad*tiempo_de_viaje)/self.rendimiento)
          return 0
    def autonomia(self):
       return self.rendimiento*self.nivel_estanque
    
    def llenar_estanque(self,litros):
       if self.nivel_estanque+litros>self.capacidad_estanque:
          return False
       else:
          self.nivel_estanque=self.nivel_estanque+litros
          return (self.nivel_estanque,True)

if __name__ == "__main__":
    auto=Auto(100,12)
         