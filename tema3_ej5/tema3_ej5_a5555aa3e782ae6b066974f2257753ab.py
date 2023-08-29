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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_maximos = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_maximos:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_maximos, False


if __name__ == "__main__":
    auto = Auto(100, 12)

    viaje = [(60, 2), (80, 3), (50, 4)]  # Velocidad y tiempo en cada tramo del viaje
    paradas = 0

    for velocidad, tiempo in viaje:
        parada = auto.andar(velocidad, tiempo)
        if parada > 0:
            paradas += 1
            print("Se quedó sin combustible, faltaron recorrer {parada} km.")

    print("Paradas para cargar combustible: {paradas}")