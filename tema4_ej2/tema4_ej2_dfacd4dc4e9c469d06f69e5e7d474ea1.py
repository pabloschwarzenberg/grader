class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.capacidad_estanque = capacidad_estanque
        self.rendimiento = rendimiento
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.nivel_estanque = 0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def autonomia(self):
        return (self.rendimiento * self.nivel_estanque)

    def andar(self,velocidad,tiempo):
        self.kilometraje += velocidad * tiempo
        self.cuenta_kilometros += velocidad * tiempo
        if self.nivel_estanque > velocidad * tiempo / self.rendimiento:
            self.nivel_estanque -= velocidad * tiempo / self.rendimiento
            return 0
        else:
            self.nivel_estanque = 0
            return (velocidad * tiempo / self.rendimiento - self.nivel_estanque)*velocidad
    def llenar_estanque(self,litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque - self.nivel_estanque,False)


if __name__ == "__main__":
    auto = Auto(100,12)