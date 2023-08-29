class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
      self.cuentakilometros=0
      return
    def andar(self,velocidad,tiempo):
      distancia=velocidad*tiempo
      if distancia<=self.nivel_estanque*12:
        litros_consumidos=distancia/12
        self.nivel_estanque-=litros_consumidos
        self.kilometraje+=distancia
        self.cuenta_kilometros+=distancia
        return 0
      else:
        self.nivel_estanque=0
        self.kilometraje+=self.nivel_estanque*12
        self.cuenta_kilometros+=self.nivel_estanque*12
        return distancia-self.nivel_estanque*12
    def autonomia(self):
      return self.nivel_estanque*12
    def llenar_estanque(self,litros):
      if self.capacidad_estanque>=self.nivel_estanque+litros:
        self.nivel_estanque+=litros
        t=(self.nivel_estanque,True)
      else:
        t=(self.capacidad_estanque-self.nivel_estanque,False)      
if __name__ == "__main__":
  auto=Auto(100,12)
         