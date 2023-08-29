class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return True

    def autonomia(self):
        kilometros=self.nivel_estanque*self.rendimiento
        return kilometros

    def llenar_estanque(self,litros):
        x=self.nivel_estanque+litros
        if x<=self.capacidad_estanque:
            self.nivel_estanque=x
            return(self.capacidad_estanque,True)

        else:
            y=self.capacidad_estanque-self.nivel_estanque
            return (y,False)

    def andar(self,velocidad,tiempo):
        distancia_total=velocidad*tiempo
        distancia_realizable=self.nivel_estanque*self.rendimiento
        if distancia_realizable>=distancia_total:
            self.nivel_estanque=(distancia_realizable-distancia_total)/self.rendimiento
            return 0
        else:
            falta=distancia_total-distancia_realizable
            return falta
if __name__ == "__main__":
    auto=Auto(100,12)
         