class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.kilometraje=0
    def andar(self,velocidad,tiempo):
        self.velocidad=velocidad
        self.tiempo=tiempo
        distancia=self.velocidad*self.tiempo
        if distancia>self.rendimiento*self.nivel_estanque:
          distancia_faltante=distancia-self.rendimiento*self.nivel_estanque
          self.nivel_estanque=0
          return distancia_faltante
        else:
          self.nivel_estanque=self.nivel_estanque-(distancia/self.rendimiento)
          return 0
        
    def autonomia(self):
        aut=self.nivel_estanque*self.rendimiento
        return aut
    def llenar_estanque(self,litros):
        self.litros=litros
        if self.nivel_estanque+self.litros>self.capacidad_estanque:
          return (100,False)
        else:
          self.nivel_estanque=self.nivel_estanque+self.litros
          return (self.nivel_estanque,True)
        
        

if __name__ == "__main__":
    auto=Auto(100,12)
         