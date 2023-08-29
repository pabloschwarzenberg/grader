class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
      self.capacidad_estanque=capacidad_estanque
      self.rendimiento=rendimiento
    
    def __reiniciar_cuentakilometros(self,cuenta_kilometros):
      self.cuenta_kilometros=cuenta_kilometros
      if cuenta_kilometros !=0:
        reiniciar= cuenta_kilometros=0
        print (reiniciar)
      else:
        print("No se puede reiniciar porque los kilometros son 0")
    
    def __andar__(self,velocidad,tiempo):
      self.velocidad=velocidad
      self.tiempo=tiempo

if __name__ == "__main__":
    auto=Auto(100,12)
         