class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilomeros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        gasto=distancia/self.rendimiento
        if self.nivel_estanque-gasto<0:
            return self.autonomia()
        else:
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            self.nivel_estanque-=gasto
            return 0
    def autonomia(self):
        queda=self.nivel_estanque*self.rendimiento
        return queda
    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros<=self.capacidad_estanque:
            self.nivel_estanque+=litros
            return (self.nivel_estanque,True)
        else:
            return(self.capacidad_estanque,False)

if __name__ == "__main__":
    auto=Auto(100,12)
         