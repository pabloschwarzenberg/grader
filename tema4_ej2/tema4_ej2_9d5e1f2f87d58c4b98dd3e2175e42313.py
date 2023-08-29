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
            self.kilometraje += distancia - km_faltantes
            self.cuenta_kilometros += distancia - km_faltantes
            self.nivel_estanque = 0
            return km_faltantes

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

    distancia_viaje = 500  # Kilómetros del viaje
    tiempo_viaje = 10  # Horas de duración del viaje

    paradas_carga = 0  # Contador de paradas de carga de combustible

    while distancia_viaje > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual < distancia_viaje:
            paradas_carga += 1
            litros_a_cargar, exito = auto.llenar_estanque(auto.capacidad_estanque)
            distancia_viaje -= autonomia_actual
            auto.reiniciar_cuentakilometros()
        else:
            auto.andar(distancia_viaje, tiempo_viaje)
            distancia_viaje = 0

    print("Paradas de carga de combustible:", paradas_carga)
