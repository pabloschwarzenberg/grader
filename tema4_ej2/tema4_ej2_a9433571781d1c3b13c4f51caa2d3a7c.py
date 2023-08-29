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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_viaje = 500  # Distancia total del viaje en kilómetros
    paradas_carga = 0  # Inicialmente no se han hecho paradas de carga

    while distancia_viaje > 0:
        autonomia = auto.autonomia()
        if autonomia < distancia_viaje:
            parada = auto.llenar_estanque(auto.capacidad_estanque)
            if parada[1]:  # Si se pudo llenar el estanque
                paradas_carga += 1
                distancia_viaje -= autonomia
            else:
                distancia_viaje -= parada[0] * auto.rendimiento
        else:
            distancia_viaje = 0

    print("Número de paradas de carga:", paradas_carga)