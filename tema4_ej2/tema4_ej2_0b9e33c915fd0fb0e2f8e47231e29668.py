class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        d = velocidad * tiempo
        k = self.nivel_estanque * self.rendimiento
        l = d/self.rendimiento

        if d > k:
            h = d - k

        if d <= k:
            self.nivel_estanque = self.nivel_estanque - l
            self.cuenta_kilometros = self.cuenta_kilometros + d
            self.kilometraje = self.kilometraje + k
            return 0

    def autonomia(self):
        s = self.nivel_estanque * self.rendimiento
        return s

    def llenar_estanque(self, cant_litros):
        if self.nivel_estanque == 0 and (cant_litros > self.capacidad_estanque):
            return self.capacidad_estanque, False

        elif self.nivel_estanque == 0 and (cant_litros <= self.capacidad_estanque):
            self.nivel_estanque += cant_litros
            return self.nivel_estanque, True

        elif self.nivel_estanque != 0 and ((cant_litros + self.nivel_estanque) <= self.capacidad_estanque):
            self.nivel_estanque += cant_litros
            return (self.nivel_estanque), True

        elif self.nivel_estanque != 0 and ((cant_litros + self.nivel_estanque >= self.capacidad_estanque)):

            return (self.capacidad_estanque - self.nivel_estanque), False



if __name__ == "__main__":
    auto=Auto(100,12)
         