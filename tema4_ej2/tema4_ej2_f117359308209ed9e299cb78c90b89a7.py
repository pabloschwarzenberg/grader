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
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    distancia_viaje = 500  # Distancia del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio del viaje en km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo estimado del viaje en horas

    paradas_carga = 0
    while distancia_viaje > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual < distancia_viaje:
            paradas_carga += 1
            litros_carga, exito = auto.llenar_estanque(auto.capacidad_estanque)
            if exito:
                distancia_viaje -= autonomia_actual
                auto.andar(velocidad_viaje, tiempo_viaje)
            else:
                distancia_viaje -= litros_carga * auto.rendimiento
                auto.andar(velocidad_viaje, tiempo_viaje)
                break
        else:
            auto.andar(velocidad_viaje, tiempo_viaje)
            distancia_viaje = 0

    print("Paradas de carga necesarias:", paradas_carga)
