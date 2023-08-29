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
        combustible_necesario = distancia / self.rendimiento
        if combustible_necesario <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= combustible_necesario
            return 0
        else:
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            distancia_faltante = distancia - distancia_recorrida
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad):
        if cantidad <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad
            return self.nivel_estanque, True
        else:
            max_cantidad = self.capacidad_estanque - self.nivel_estanque
            return max_cantidad, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    viaje_distancia = 500  # km
    viaje_velocidad = 80  # km/h
    viaje_tiempo = viaje_distancia / viaje_velocidad  # horas

    paradas = 0
    while True:
        faltante = auto.andar(viaje_velocidad, viaje_tiempo)
        if faltante > 0:
            paradas += 1
            auto.llenar_estanque(auto.autonomia())
        else:
            break

    print("Número de paradas necesarias:", paradas)