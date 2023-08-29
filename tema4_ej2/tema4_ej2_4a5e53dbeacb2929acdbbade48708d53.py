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
        distancia=velocidad*tiempo
        self.kilometraje=self.kilometraje+distancia
        self.cuenta_kilometros=self.cuenta_kilometros+distancia
        litros_necesarios=distancia/self.rendimiento        
        if(self.nivel_estanque-litros_necesarios>=0):
            self.nivel_estanque=self.nivel_estanque-litros_necesarios
            return 0
        else:
            return(distancia-self.nivel_estanque*self.rendimiento)               
    def autonomia(self):
        return(self.nivel_estanque*self.rendimiento)
    def llenar_estanque(self,litros):
        a=litros+self.nivel_estanque
        if(a>self.capacidad_estanque):
            return(self.capacidad_estanque,False)
        else:
            self.nivel_estanque=a
            return(self.nivel_estanque,True)


if __name__ == "__main__":
    auto=Auto(100,12)
         