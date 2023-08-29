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
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque > self.capacidad_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False
        else:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True


if __name__ == "__main__":
    auto = Auto(100, 12)

    velocidad_viaje = 80
    tiempo_viaje = 4
    detenciones = 0

    while True:
        distancia_restante = auto.andar(velocidad_viaje, tiempo_viaje)
        if distancia_restante == 0:
            break
        detenciones += 1

    print("Detenciones necesarias durante el viaje:", detenciones)

         