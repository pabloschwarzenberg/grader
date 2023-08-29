class Auto:
  def __init__(self, capacidad_estanque, rendimiento):
    self.capacidad_estanque=int(capacidad_estanque)
    self.rendimiento=int(rendimiento)
    self.kilometraje=0
    self.cuentakilometros=0
    self.nivel_estanque=0
  def reiniciar_cuentakilometros(self):
    self.cuentakilometros=0
  def andar(self,velocidad,tiempo):
    if (int(velocidad)*int(tiempo))>(self.rendimiento*self.nivel_estanque):
      kilometros=self.rendimiento*self.nivel_estanque
      self.nivel_estanque=0
      self.kilometraje += kilometros
      self.cuentakilometros += kilometros
      por_recorrer=(int(velocidad)*int(tiempo))-(self.rendimiento*self.nivel_estanque)
      return por_recorrer
    else:
      kilometros=int(velocidad)*int(tiempo)
      self.nivel_estanque -= kilometros/self.rendimiento
      self.kilometraje += kilometros
      self.cuentakilometros += kilometros
      return 0
  def llenar_estanque(self,litros):
    litros=int(litros)
    if (self.nivel_estanque+litros)<=self.capacidad_estanque:
      self.nivel_estanque += litros
      return self.nivel_estanque,True
    else:
      puede_echar=self.capacidad_estanque-self.nivel_estanque
      return puede_echar,False
  def autonomia(self):
    autonomia=self.nivel_estanque*self.rendimiento
    return autonomia