class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
    self.kilometraje = 0
    self.cuenta_kilometros = 0
    self.capacidad_estanque = capacidad_estanque
    self.nivel_estanque = 0
    self.rendimiento = rendimiento

  def reiniciar_cuentakilometros(self):
    self.cuenta_kilometros = 0
    return self.cuenta_kilometros

  def andar(self, velocidad, tiempo):
    distancia = velocidad * tiempo
    self.kilometraje += distancia 
    self.cuenta_kilometros += distancia
    litros_viaje = (distancia/ self.rendimiento)

    if litros_viaje < self.nivel_estanque:
      restante = distancia - (self.rendimiento * self.nivel_estanque)
      self.nivel_estanque -= (distancia / self.rendimiento)
      return restante
    else:
      self.nivel_estanque -= (distancia / self.rendimiento)
      return 0


  def autonomia(self):
    autono = self.rendimiento * self.nivel_estanque
    return autono


  def llenar_estanque(self, cant_litros):
    litros = self.nivel_estanque + cant_litros
    if litros > self.capacidad_estanque:
      return self.capacidad_estanque, False
    else:
      self.nivel_estanque += litros 
      return self.nivel_estanque, True

if __name__ == "__main__":
    auto=Auto(100,12)
         