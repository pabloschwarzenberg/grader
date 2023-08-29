class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
    self.kilometraje = 0
    self.cuenta_kilometros = 0
    self.capacidad_estanque = capacidad_estanque
    self.nivel_estanque = 0
    self.rendimiento = rendimiento
    
  def reiniciar_cuentakilometros(self):
    self.cuenta_kilometros = 0
  
  def andar(self, velocidad, tiempo):
    self.nivel_estanque -= (velocidad * tiempo) / self.rendimiento
    self.cuenta_kilometros += velocidad * tiempo
    self.kilometraje += velocidad * tiempo
  
  def autonomia(self):
    return self.nivel_estanque * self.rendimiento

  def llenar_estanque(self, cantidad_de_litros):
    litros_actuales = self.nivel_estanque + cantidad_de_litros
    if litros_actuales > self.capacidad_estanque:
      return (self.capacidad_estanque - self.nivel_estanque, False)
    else:
      self.nivel_estanque = litros_actuales
      return (litros_actuales, True)

if __name__ == "__main__":
    auto=Auto(100,12)