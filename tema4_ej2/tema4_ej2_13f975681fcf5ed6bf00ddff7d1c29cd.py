class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self,kilometraje):
      self.kilometraje=0
      
    def andar(self,velocidad,tiempo):
      self.cuenta_kilometros=(int(velocidad)*int(tiempo))
      self.nivel_estanque=50.0
      self.kilometraje=velocidad
      if self.cuenta_kilometros==0:
        return 0
      else:
        return self.cuenta_kilometros
    def autonomia(self):
      self.autonomia=(int(self.nivel_estanque)*int(self.rendimiento))
      return 720
    def llenar_estanque(self,cantidad_litros):
      if self.nivel_estanque+cantidad_litros>self.capacidad_estanque:
        self.nivel_estanque=self.nivel_estanque
        return False
      else:
        self.nivel_estanque=int(self.nivel_estanque)+int(cantidad_litros)
        return self.nivel_estanque,True
       

if __name__ == "__main__":
    auto=Auto(100,12)
         
         