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
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_necesarios
            return 0
        else:
            faltante = litros_necesarios - self.nivel_estanque
            self.kilometraje += distancia - (faltante * self.rendimiento)
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 1000  # Distancia total del viaje en kilómetros
    paradas = 0

    while distancia_viaje > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual < distancia_viaje:
            distancia_recorrida = autonomia_actual
            faltante = auto.andar(100, distancia_recorrida / 100)
            paradas += 1
            if faltante > 0:
                litros_necesarios = faltante * auto.rendimiento
                auto.llenar_estanque(litros_necesarios)
        else:
            auto.andar(100, distancia_viaje / 100)
            distancia_viaje = 0

    print("Número de paradas:", paradas)