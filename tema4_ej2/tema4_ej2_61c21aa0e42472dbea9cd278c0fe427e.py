class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo_de_viaje):
        km_viaje = velocidad * tiempo_de_viaje
        if km_viaje <= self.autonomia():
            self.cuenta_kilometros = km_viaje
            self.kilometraje += self.cuenta_kilometros
            self.nivel_estanque -= km_viaje / self.rendimiento
            self.reiniciar_cuentakilometros()
            return 0
        else:
            self.cuenta_kilometros = self.autonomia()
            self.kilometraje += self.cuenta_kilometros
            self.nivel_estanque = 0
            self.reiniciar_cuentakilometros()
            return km_viaje - self.autonomia()

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros < self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return [self.nivel_estanque, True]
        else:
            return [self.capacidad_estanque - self.nivel_estanque, False]


if __name__ == "__main__":
    auto = Auto(100, 12)
