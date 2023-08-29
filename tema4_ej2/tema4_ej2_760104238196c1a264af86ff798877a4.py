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
        distancia = velocidad * tiempo
        posible = self.nivel_estanque * self.rendimiento
        if posible > distancia:
            self.nivel_estanque -= distancia / self.rendimiento
            self.cuenta_kilometros += distancia
            self.kilometraje += distancia
            return 0
        else:
            self.cuenta_kilometros += posible
            self.kilometraje += posible
            self.nivel_estanque = 0
            return distancia - posible

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
        return min(self.nivel_estanque + litros, self.capacidad_estanque), self.nivel_estanque + litros > self.capacidad_estanque



if __name__ == "__main__":
    auto = Auto(100, 12)
