class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
      
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo_viaje):
        distancia1=velocidad*tiempo_viaje
        distancia2=self.rendimiento*self.nivel_estanque
        combustible_utilizado=distancia1/self.rendimiento
        self.nivel_estanque-=combustible_utilizado
        self.kilometraje+=distancia1
        self.cuenta_kilometros+=distancia1
        if self.nivel_estanque>0:
            return 0
        else:
            a=distancia1-distancia2
            return a
          
    def autonomia(self):
        distancia2=self.rendimiento*self.nivel_estanque
        return distancia2
        
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros>self.capacidad_estanque:
            return False
        else:
            a=self.nivel_estanque+litros
            self.nivel_estanque+=a
            return a
            return True
        

if __name__ == "__main__":
    auto=Auto(100,12)
         