class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
    self.kilometraje = 0
    self.cuenta_kilometros = 0
    self.capacidad_estanque = capacidad_estanque
    self.nivel_estanque = 0
    self.rendimiento = rendimiento 
  
  def reiniciar_cuenta_kilometros(self):
    self.cuenta_kilometros = 0
    
  def andar (self, velocidad, tiempo_viaje):
    distancia_recorrida = velocidad * tiempo_viaje
    litros_gastados = distancia_recorrida / self.rendimiento
    
    if litros_gastados <= self.nivel_estanque:
      self.kilometraje += distancia_recorrida
      self.cuenta_kilometros += distancia_recorrida
      self.nivel_estanque -= litros_gastados
      return 0
    else:
      distancia_faltante = (litros_gastados - self.nivel_estanque) * self.rendimiento
      self.kilometraje += distancia_recorrida - distancia_faltante
      self.cuenta_kilometros += distancia_recorrida - distancia_faltante
      self.nivel_estanque = 0
      return distancia_faltante
    
  def autonomia(self):
    return self.nivel_estanque * self.rendimiento
  
  def llenar_estanque(self, cantidad_litros):
    if cantidad_litros > self.capacidad_estanque:
      return self.capacidad_estanque
      False
    else:
      self.nivel_estanque = cantidad_litros
      return self.nivel_estanque 
      True
      
if __name__ == "__main__":
  auto=Auto(100,12)
  distancia_total = 1000
  velocidad_viaje = 100
         