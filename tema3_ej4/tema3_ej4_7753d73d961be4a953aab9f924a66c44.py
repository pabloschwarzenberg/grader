#9
class Fraccion:
  def __init__(self, numerador, denominador):
    self.numerador = numerador
    self.denominador = denominador
    
  
  def mcm(self, other):
    # Obtenemos el maximo y el minimo de los denominadores
    mas_grande = max(self.denominador, other.denominador)
    mas_peque = min(self.denominador, other.denominador)
    # Mientras el menor sea mayor que 0, seguimos iterando
    
    while mas_peque:
      mcd = mas_peque
      mas_peque = mas_grande % mas_peque
      mas_grande = mcd
    return (self.denominador * other.denominador) // mcd
      
    
    return self.denominador * other.denominador // self.mcd(other)
  
  def __add__(self, other):
    return Fraccion(self.numerador * (self.mcm(other) // self.denominador) + other.numerador * (self.mcm(other) // other.denominador), self.mcm(other))
  
  def __sub__(self, other):
    return Fraccion(self.numerador * (self.mcm(other) // self.denominador) - other.numerador * (self.mcm(other) // other.denominador), self.mcm(other))
  
  def __mul__(self, other):
    return Fraccion(self.numerador * other.numerador, self.denominador * other.denominador)

  def __truediv__(self, other):
    return Fraccion(self.numerador * other.denominador, self.denominador * other.numerador)

  def __str__(self):
    return str(self.numerador) + "/" + str(self.denominador)
  
  def a_numero(self):
    return self.numerador / self.denominador
  
if __name__ == "__main__":
  d1 = Fraccion(1, 2)
  d2 = Fraccion(1, 3)
  print(d1 + d2)
  