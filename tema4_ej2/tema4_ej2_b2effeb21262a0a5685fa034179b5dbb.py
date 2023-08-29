class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque =0
        self.rendimiento= rendimiento
        self.capacidad_estanque = capacidad_estanque
    def reiniciar_cuentakilometros():
        self.kilometraje=0
    def andar(self, velocidad, tiempo):
        self.kilometraje+=velocidad*tiempo
        self.cuenta_kilometros =velocidad*tiempo
        self.nivel_estanque-=self.cuenta_kilometros/self.rendimiento
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    def llenar_estanque(self, litros):
        if litros+self.nivel_estanque<= self.capacidad_estanque:
            self.nivel_estanque+=litros
            return(self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque, False)

if __name__ == "__main__":
    auto=Auto(100,12)