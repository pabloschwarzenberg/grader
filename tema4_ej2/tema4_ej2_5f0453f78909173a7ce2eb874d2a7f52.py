class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        pass
    kilometraje=0
    cuenta_kilometros=0
    nivel_estanque=0
    def andar(self,velocidad,tiempo):
      if (self.nivel_estanque-(tiempo*velocidad/self.rendimiento))>=0:
        self.nivel_estanque=self.nivel_estanque-(tiempo*velocidad/self.rendimiento)
        return 0
      else:
        return -1*((self.nivel_estanque-(tiempo*velocidad/self.rendimiento)/self.rendimiento))
        
    def reiniciar_cuentakilometros(self):
      self.cuenta_kilometros=0
      pass
    def autonomia(self):
      return (self.nivel_estanque*self.rendimiento)
    def llenar_estanque(self,litros):
      if litros>self.capacidad_estanque-self.nivel_estanque:
        return self.capacidad_estanque-self.nivel_estanque,False
      else:
        self.nivel_estanque+=litros
        return self.nivel_estanque+litros,True
        

if __name__ == "__main__":
    auto=Auto(100,12)
         