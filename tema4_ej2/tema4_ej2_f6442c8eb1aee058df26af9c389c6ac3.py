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

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    estanque_capacidad = 100
    rendimiento = 12

    auto = Auto(estanque_capacidad, rendimiento)

    distancia_viaje = 500  # Distancia total del viaje en kilómetros
    velocidad_viaje = 80  # Velocidad promedio en km/h

    veces_carga = 0

    while distancia_viaje > 0:
        autonomia_actual = auto.autonomia()
        if autonomia_actual < distancia_viaje:
            veces_carga += 1
            distancia_recorrida = distancia_viaje - autonomia_actual
            tiempo_restante = distancia_recorrida / velocidad_viaje
            auto.andar(velocidad_viaje, tiempo_restante)
            litros_a_cargar = estanque_capacidad - auto.nivel_estanque
            auto.llenar_estanque(litros_a_cargar)
            auto.reiniciar_cuentakilometros()
            distancia_viaje -= autonomia_actual
        else:
            auto.andar(velocidad_viaje, distancia_viaje)
            distancia_viaje = 0

    print("Número de veces que se detuvo a cargar combustible:", veces_carga)
