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
            kilometros_restantes = (self.nivel_estanque * self.rendimiento) - distancia
            self.nivel_estanque = 0
            self.kilometraje += distancia - kilometros_restantes
            self.cuenta_kilometros += distancia - kilometros_restantes
            return kilometros_restantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    velocidad = 80
    tiempo = 2
    detenciones = 0

    while True:
        resultado = auto.andar(velocidad, tiempo)
        if resultado == 0:
            break
        else:
            detenciones += 1
            auto.llenar_estanque(auto.autonomia())

    print("Número de detenciones: ", detenciones)
