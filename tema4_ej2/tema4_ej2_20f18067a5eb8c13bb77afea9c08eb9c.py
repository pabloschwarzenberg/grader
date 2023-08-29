class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def llenar_estanque(self,litros):   #ok
        if litros<=self.capacidad_estanque:
            self.nivel_estanque=litros
            return self.nivel_estanque,True
        else:
            return self.capacidad_estanque,False
    def reiniciar_cuentakilometros(self):  #ok
        self.cuenta_kilometros=0
    def autonomia(self):  #ok
        return self.nivel_estanque*self.rendimiento
    def andar(self,velocidad,tiempo):
        self.cuenta_kilometros=velocidad*tiempo
        self.kilometraje=velocidad*tiempo
        if self.nivel_estanque*self.rendimiento>=velocidad*tiempo:
            self.nivel_estanque=self.nivel_estanque-velocidad*tiempo/self.rendimiento
            return 0
        else:
            self.nivel_estanque=0
            return velocidad*tiempo-self.nivel_estanque*self.rendimiento
        
        
     

if __name__ == "__main__":
    auto=Auto(100,12)
    auto.llenar_estanque(60)
    auto.andar(120,1)
         