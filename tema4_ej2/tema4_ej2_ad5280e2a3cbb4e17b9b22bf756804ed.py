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
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


if __name__ == "__main__":
    auto = Auto(100, 12)
    distancia_viaje = 500  # km
    velocidad_viaje = 80  # km/h
    tiempo_viaje = distancia_viaje / velocidad_viaje  # horas

    num_paradas = 0
    while distancia_viaje > 0:
        falta_combustible = auto.andar(velocidad_viaje, tiempo_viaje)
        if falta_combustible > 0:
            num_paradas += 1
            litros_a_cargar, _ = auto.llenar_estanque(falta_combustible)
            distancia_viaje = litros_a_cargar * auto.rendimiento
        else:
            distancia_viaje = 0

    print("Cantidad de paradas necesarias: ", num_paradas)

         