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
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += km_faltantes
            self.cuenta_kilometros += km_faltantes
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            return self.capacidad_estanque, False

        self.nivel_estanque += litros
        if self.nivel_estanque > self.capacidad_estanque:
            self.nivel_estanque = self.capacidad_estanque

        return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_total = 1000  # Distancia total del viaje en kilómetros
    paradas = 0

    while distancia_total > 0:
        autonomia_actual = auto.autonomia()

        if autonomia_actual >= distancia_total:
            distancia_total = 0
        else:
            distancia_total -= autonomia_actual
            paradas += 1
            auto.llenar_estanque(auto.capacidad_estanque)

    print("Debes detenerte a cargar combustible", paradas, "veces en el viaje.")
