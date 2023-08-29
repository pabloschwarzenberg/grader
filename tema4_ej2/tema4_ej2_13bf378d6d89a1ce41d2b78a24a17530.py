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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            return distancia_faltante

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

    distancia_viaje = float(input("Ingrese la distancia del viaje en kilómetros: "))

    detenciones = 0
    while distancia_viaje > 0:
        autonomia = auto.autonomia()

        if autonomia >= distancia_viaje:
            auto.andar(100, distancia_viaje)
            distancia_viaje = 0
        else:
            distancia_recorrida = auto.andar(100, autonomia)
            distancia_viaje -= distancia_recorrida
            detenciones += 1
            litros_a_cargar = auto.capacidad_estanque - auto.nivel_estanque
            auto.llenar_estanque(litros_a_cargar)

    print("Número de detenciones requeridas:", detenciones)
