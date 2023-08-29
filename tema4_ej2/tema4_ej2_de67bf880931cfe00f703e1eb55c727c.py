class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self,cuenta_kilometros):
        self.cuenta_kilometros=cuenta_kilometros
        cuenta_kilometros=0
        return cuenta_kilometros
        
    def andar(self,velocidad,tiempo_viaje):
        if self.nivel_estanque*self.rendimiento>=velocidad*tiempo_viaje:
            self.cuenta_kilometros+=velocidad*tiempo_viaje
            self.kilometraje+=velocidad*tiempo_viaje
            self.nivel_estanque-=(velocidad*tiempo_viaje)/self.rendimiento
            return 0
        else:
            self.cuenta_kilometros+=self.nivel_estanque*self.rendimiento
            self.kilometraje+=self.nivel_estanque*self.rendimiento
            y=velocidad*tiempo_viaje-self.nivel_estanque*self.rendimiento
            self.nivel_estanque=0
            return y
            
        


    def autonomia(self):
        autonomia=self.rendimiento*self.nivel_estanque
        return autonomia       


    def llenar_estanque(self,cantidad_litros):
        if self.nivel_estanque+cantidad_litros<=self.capacidad_estanque:
            self.nivel_estanque+=cantidad_litros
            return self.nivel_estanque, True
        else:
            y=self.capacidad_estanque-self.nivel_estanque
            return y,False
           
        


if __name__ == "__main__":
    auto=Auto(100,12)
         


