class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.cuenta_kilometros=0
        self.nivel_estanque=0
        self.kilometraje=0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
  
       
    def andar(self,velocidad,tiempo_viaje):
        kilometros_recorridos=(velocidad*tiempo_viaje)
        litros_gastados=kilometros_recorridos/self.rendimiento
        self.cuenta_kilometros+=kilometros_recorridos
        self.kilometraje+=kilometros_recorridos
        self.nivel_estanque-=litros_gastados
        if self.nivel_estanque<0:
           faltaron=abs(self.nivel_estanque)
           noalcanzoarecorrer=faltaron*self.rendimiento
           return noalcanzoarecorrer
        else:
           return 0
    def autonomia(self):
         autonomia=self.nivel_estanque*self.rendimiento
         return autonomia
       
    def llenar_estanque(self,litros):
        self.nivel_estanque+=litros
        if self.nivel_estanque>self.capacidad_estanque:
           self.nivel_estanque-=litros
           return (self.capacidad_estanque,False)
        else:
            return (self.nivel_estanque,True)
            

if __name__ == "__main__":
    auto=Auto(100,12)
         