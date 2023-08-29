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
            km_faltantes = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - km_faltantes
            self.cuenta_kilometros += distancia - km_faltantes
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque:
            litros = self.capacidad_estanque
        self.nivel_estanque = litros


if __name__ == "__main__":
    auto = Auto(60, 12)

    # Llenar el estanque con 60 litros
    auto.llenar_estanque(60)

    # Mostrar la autonomía actual del auto
    print("Autonomía:", auto.autonomia())

    # Viajar a 120 km/h durante 1 hora
    velocidad = 120  # km/h
    tiempo = 1  # horas
    auto.andar(velocidad, tiempo)

    # Mostrar el nivel actual del estanque
    print("Estanque:", auto.nivel_estanque, "litros")
    print("Rendimiento:", auto.rendimiento, "km/l")
