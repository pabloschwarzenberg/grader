class Auto:
    kilomentraje = 0
    cuentra_kilomentra = 0
    nivel_estanque = 0
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento

    def reiniciar_cuenta_kilometros(self):
        self.cuentra_kilomentra = 0

    def andar(self, v, t):
        self.nivel_estanque = 50
        self.rendimiento = 12
        return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, mas_gasolina):
        calcular =  mas_gasolina + self.nivel_estanque
        if self.capacidad_estanque >= calcular:
            self.nivel_estanque = calcular
            return self.nivel_estanque
        else:
            return (self.capacidad_estanque, False)

if __name__ == "__main__":
    auto=Auto(100,12)
         