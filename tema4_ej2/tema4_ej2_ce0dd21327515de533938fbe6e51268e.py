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
        combustible_necesario = distancia / self.rendimiento

        if combustible_necesario <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= combustible_necesario
            return 0
        else:
            distancia_restante = (self.nivel_estanque * self.rendimiento) - self.cuenta_kilometros
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            self.nivel_estanque = 0
            return distancia - distancia_restante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque - self.nivel_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            self.nivel_estanque = self.capacidad_estanque
            return max_litros, False
        else:
            self.nivel_estanque += litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(100, 12)
