class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        if self.nivel_estanque-velocidad*tiempo*(1/self.rendimiento)>=0:
            self.kilometraje+=velocidad*tiempo
            self.cuenta_kilometros+=velocidad*tiempo
            self.nivel_estanque-=velocidad*tiempo*(1/self.rendimiento)
            return(0)
        else:
            recorrido=self.rendimiento*self.nivel_estanque
            falta=(velocidad*tiempo)-recorrido
            self.kilometraje+=recorrido
            self.cuenta_kilometros+=recorrido
            self.nivel_estanque=0
            return(falta)
        
    
    def autonomia(self):
        return(self.rendimiento*self.nivel_estanque)
    
    def llenar_estanque(self,litros):
        maxallenar=self.capacidad_estanque-self.nivel_estanque
        if litros>maxallenar:
            return((maxallenar,False))
        else:
            self.nivel_estanque+=litros
            return((self.nivel_estanque,True))

if __name__ == "__main__":
    auto=Auto(100,12)
         