class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
      self.nivel_estanque= 0
      self.kilometraje = 0
      self.cuenta_kilometros = 0
 
if __name__ == "__main__":
    auto=Auto(100,12)
         