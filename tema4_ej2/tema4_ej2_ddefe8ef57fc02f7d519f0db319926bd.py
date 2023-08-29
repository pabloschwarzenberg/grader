class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
    self.kilometraje = 0
    self.cuenta_kilometros = 0
    self.capacidad_estanque = capacidad_estanque
    self.nivel_estanque = 0
    self.rendimiento = rendimiento
    
  def reiniciar_cuentakilometros(self):
    self.cuenta_kilometros = 0
  
  def andar(self,v,t):
    d = v * t
    a = self.autonomia()
    ar = a - d
    if ar >= 0:
      self.nivel_estanque = ar / self.rendimiento
      self.kilometraje += d
      self.cuenta_kilometros += d
      return 0
    else:
      self.nivel_estanque = 0
      self.kilometraje += a
      self.cuenta_kilometros += a
      return ar * -1
   
  def autonomia(self):
    return self.nivel_estanque * self.rendimiento
  
  def llenar_estanque(self,lit):
    mc = self.capacidad_estanque - self.nivel_estanque
    if mc < lit:
      return (mc, False)
    else:
      self.nivel_estanque += lit
      return (self.nivel_estanque, True)
    
  
        

if __name__ == "__main__":
    auto=Auto(100,12)
         