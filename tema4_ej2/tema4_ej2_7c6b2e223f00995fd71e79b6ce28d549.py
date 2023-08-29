class Auto:
    def __init__(self,capacidad,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros():
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        litros=(velocidad*tiempo)/self.rendimiento
        if litros<=self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque-litros
            self.kilometraje+=velocidad*tiempo
            self.cuenta_kilometros+=velocidad*tiempo
            return 0
        else:
            self.kilometraje+=self.nivel_estanque*self.rendimiento
            self.cuenta_kilometros+=self.nivel_estanque*self.rendimiento
            self.nivel_estanque=0
            return litros-self.nivel_estanque

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento

    def llenar_estanque(self,litros):
        if litros<=self.capacidad_estanque-self.nivel_estanque:
            self.nivel_estanque+=litros
            return (self.nivel_estanque,True)

        else:
            return (self.capacidad_estanque,False)
if __name__ == "__main__":
    auto=Auto(100,12)
         