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
        litros_consumidos = distancia / self.rendimiento

        if litros_consumidos <= self.nivel_estanque:
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            distancia_faltante = self.rendimiento * self.nivel_estanque
            self.nivel_estanque = 0
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            return distancia - distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    viaje = [
        (80, 2),  # velocidad: 80 km/h, tiempo: 2 horas
        (60, 3),  # velocidad: 60 km/h, tiempo: 3 horas
        (70, 1),  # velocidad: 70 km/h, tiempo: 1 hora
    ]

    detenciones = 0

    for velocidad, tiempo in viaje:
        detenciones += 1
        if auto.andar(velocidad, tiempo) == 0:
            detenciones -= 1

    print(f"Detenciones necesarias: {detenciones}")
