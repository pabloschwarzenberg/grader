class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        needs=distancia/self.rendimiento  #Litros
        if self.nivel_estanque<needs:
            return (needs-self.nivel_estanque)*self.rendimiento
        else:
            self.nivel_estanque-=needs
            return 0
    
    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
        
    def llenar_estanque(self,litros):
        if litros>(self.estanque-self.nivel_estanque):
            return (self.estanque-self.nivel_estanque, False)
        else:
            self.nivel_estanque+=litros
            return (self.nivel_estanque,True)
            
if __name__ == "__main__":
    auto=Auto(100,12)
         