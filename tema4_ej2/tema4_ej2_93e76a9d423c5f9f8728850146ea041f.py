class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_kilometros(self):
        sel.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        if self.nivel_estanque - (velocidad * tiempo / self.rendimiento)<0:
            x = velocidad * tiempo / self.rendimiento - self.nivel_estanque
            self.nivel_estanque = 0
            self.kilometraje += velocidad * tiempo - x
            self.cuenta_kilometros += velocidad * tiempo - x
            return x
        else:
            self.cuenta_kilometros += velocidad * tiempo
            self.kilometraje += velocidad * tiempo
            self.nivel_estanque -= velocidad * tiempo / self.rendimiento
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque > self.capacidad_estanque:
            return (False,self.capacidad_estanque - self.nivel_estanque)
        else:
            self.nivel_estanque += litros
            return (True,self.nivel_estanque)


if __name__ == "__main__":
    auto = Auto(100, 12)
         