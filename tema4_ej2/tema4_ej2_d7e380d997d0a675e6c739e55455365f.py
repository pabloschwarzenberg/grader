class Auto:
  def __init__(self,capacidad_estanque,rendimiento):
    self.capacidad_estanque = capacidad_estanque
    self.rendimiento = rendimiento
    self.cuenta_kilometros = 0 
    self.kilometraje = 0
    self.nivel_estanque = 0
  
  def reiniciar_cuentakilometros(self):
    cuenta_kilometros = 0
  
  def andar(self,velocidad,tiempo_de_viaje):
    self.velocidad = velocidad
    self.tiempo_de_viaje = tiempo_de_viaje
    distancia = (self.tiempo_de_viaje * self.velocidad)
    self.kilometraje += distancia
    self.cuenta_kilometros += distancia
    gas = distancia / self.rendimiento
    self.nivel_estanque -= gas
    k = distancia - self.autonomia 
    if k >= 0:
      return 0
    else:
      return k*-1
  
  def autonomia(self):
    self.autonomia = self.nivel_estanque * self.rendimiento
    return self.autonomia    
  
  def llenar_estanque(self,cantidad_de_litros):
    self.cantidad_de_litros = cantidad_de_litros
    self.nivel_estanque =+ self.cantidad_de_litros    
    if self.nivel_estanque > self.capacidad_estanque:
      tupla = (self.capacidad_estanque)
      return tupla, False
    else:
      tupla = (self.nivel_estanque)
      return tupla, True
   
    

if __name__ == "__main__":
    auto=Auto(100,12)
         