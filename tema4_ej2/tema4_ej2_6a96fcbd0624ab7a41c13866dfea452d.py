class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
                
    def andar(self, velocidad, tiempo_viaje):
        distancia = velocidad * tiempo_viaje
        consumo = distancia / self.rendimiento
        if consumo <= self.nivel_estanque:
          self.kilometraje = self.kilometraje + distancia
          self.cuenta_kilometros = self.cuenta_kilometros + distancia
          self.nivel_estanque = self.nivel_estanque - consumo
          return 0
        else:
          distancia = self.nivel_estanque  * self.rendimiento
          distancia_max = velocidad * tiempo_viaje
          self.kilometraje = self.kilometraje + distancia
          self.cuenta_kilometros = self.cuenta_kilometros + distancia
          self.nivel_estanque = 0
          return distancia_max - distancia
          
    def autonomia(self):
      return self.rendimiento * self.nivel_estanque
    
    def llenar_estanque(self, litros):
      if self.nivel_estanque + litros <= self.capacidad_estanque:
        self.nivel_estanque = self.nivel_estanque + litros
        return self.nivel_estanque, True
        
      else:
        return self.capacidad_estanque - self.nivel_estanque, False
    

if __name__ == "__main__":
    auto=Auto(100,12)
         