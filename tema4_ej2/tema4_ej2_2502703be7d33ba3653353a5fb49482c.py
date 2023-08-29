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
        litros_necesarios = distancia / self.rendimiento

        if litros_necesarios <= self.nivel_estanque:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_faltante = self.rendimiento * self.nivel_estanque
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            return distancia - distancia_faltante

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            max_litros = self.capacidad_estanque
            self.nivel_estanque = self.capacidad_estanque
            return max_litros, False
        else:
            self.nivel_estanque = litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(100, 12)

         