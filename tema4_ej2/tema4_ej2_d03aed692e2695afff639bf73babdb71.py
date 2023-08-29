class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros = 0
    def andar(self,velocidad,tiempo_de_viaje):
      distancia_km = velocidad * tiempo_de_viaje
      consumo_lt = distancia_km / self.rendimiento
      self.kilometraje += distancia_km
      self.cuenta_kilometros += distancia_km
      self.nivel_estanque -= consumo_lt 
      distancia_posible_km = self.nivel_estanque * self.rendimiento
      if distancia_km <= distancia_posible_km:
        return 0
      else:
        distancia_por_recorrer = distancia_km - distancia_posible
        return distancia_por_recorrer
    def autonomia(self):
      autonomia_auto = self.nivel_estanque * self.rendimiento
      return autonomia_auto
    def llenar_estanque(self, cantidad_de_litros):
      espacio_estanque = self.capacidad_estanque - self.nivel_estanque
      if cantidad_de_litros > espacio_estanque:
        return (self.capacidad_estanque, False)
      else:
        self.nivel_estanque += cantidad_de_litros
        return (self.nivel_estanque, True)
      
      
          
      
      
    
    
if __name__ == "__main__":
    auto=Auto(100,12)
         