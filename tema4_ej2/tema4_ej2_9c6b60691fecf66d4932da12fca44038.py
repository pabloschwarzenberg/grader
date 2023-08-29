class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
        self.kilometraje=0
        self.cuenta_kilometros=0
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometro=0
        
    def andar(self,velocidad,tiempo):
        queda=0
        self.nivel_estanque-velocidad*tiempo*1/self.rendimiento
        if self.nivel_estanque-velocidad*tiempo*1/self.rendimiento>=0:
            queda=0
            self.nivel_estanque=self.nivel_estanque-velocidad*tiempo*1/self.rendimiento
            self.kilometraje=self.kilometraje+velocidad*tiempo
            self.cuenta_kilometros=self.cuenta_kilometros+velocidad*tiempo
        elif self.nivel_estanque-velocidad*tiempo*1/self.rendimiento<0:
            queda=velocidad*tiempo-self.rendimiento*self.nivel_estanque
            self.nivel_estanque=0
        return queda
        
    def autonomia(self):
        return self.rendimiento*self.nivel_estanque
            
    def llenar_estanque(self,litros):
        estanque=(self.capacidad_estanque,False)
        if self.capacidad_estanque-self.nivel_estanque-litros<0:
            estanque=estanque
        elif self.capacidad_estanque-self.nivel_estanque-litros>=0:
            estanque=(self.nivel_estanque+litros,True)
            self.nivel_estanque=self.nivel_estanque+litros
        return estanque
          
if __name__ == "__main__":
    auto=Auto(100,12)
         