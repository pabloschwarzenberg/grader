class Auto:
    
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        kilometraje=0
        nivel_estanque=0
        cuenta_kilometros=0
    
    def autonomia(self):
      return nivel_estanque*self.rendimiento
        
    
    def andar(self,velocidad,tiempo):
        km=velocidad*tiempo
        litros_gastados=km/self.rendimiento
        if nivel_estanque-litros_gastados>=0:
          return 0
        else:
          return abs(nivel_estanque-litros_gastados)*self.rendimiento
        
    def reiniciar_cuentakilometros(self):
        cuenta_kilometros=0
        return
    
    def llenar_estanque(self,litros):
        if nivel_estanque+litros > self.capacidad_estanque:
          return self.capacidad_estanque,False
        else:
         return nivel_estanque+litros,True

if __name__ == "__main__":
    auto=Auto(100,12)
         