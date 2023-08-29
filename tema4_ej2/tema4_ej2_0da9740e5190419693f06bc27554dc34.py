class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.kilometraje=0
      self.cuenta_kilometros=0
      self.nivel_estanque=0
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
    
    def reiniciar_cuentakilometros(self):
      cuenta_kilometros=0
      

    def andar(self,velocidad,tiempo_de_viaje):
      self.velocidad=velocidad
      self.tiempo_de_viaje=tiempo_de_viaje
      dist=self.velocidad*self.tiempo_de_viaje
      litros_usados=dist/self.rendimiento
      self.nivel_estanque=self.nivel_estanque-litros_usados
      self.kilometraje=self.kilometraje+dist
      self.cuenta_kilometros=self.cuenta_kilometros+dist
      if self.nivel_estanque >= 0:
          return 0
      else:
          return self.nivel_estanque*self.rendimiento

      
    def autonomia(self):
      a=self.nivel_estanque*self.rendimiento
      return a
      

    def llenar_estanque(self,cantidad_de_litros):
      self.cantidad_de_litros=cantidad_de_litros
      self.nivel_estanque=self.cantidad_de_litros
      if self.cantidad_de_litros > self.capacidad_estanque:
          return (self.capacidad_estanque,False)
      else:
          return (self.nivel_estanque,True)

     
       

if __name__ == "__main__":
    auto=Auto(100,12)
         