class Auto:
    def __init__(self,capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        self.nivel_estanque=float(50)
        
    def autonomia(self):
        autono=self.nivel_estanque*self.rendimiento
        return autono

    def llenar_estanque(self,litros):
        if litros>self.capacidad_estanque-self.nivel_estanque:
            return self.capacidad_estanque-self.nivel_estanque,False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)
         