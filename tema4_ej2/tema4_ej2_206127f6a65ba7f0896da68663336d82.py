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
            distancia_faltante = (self.nivel_estanque * self.rendimiento) - distancia
            self.nivel_estanque = 0
            self.kilometraje += (distancia - distancia_faltante)
            self.cuenta_kilometros += (distancia - distancia_faltante)
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


if __name__ == "__main__":
    capacidad_estanque = 100
    rendimiento = 12

    auto = Auto(capacidad_estanque, rendimiento)

    viaje = 1000  # Kilómetros a recorrer en el viaje
    velocidad = 80  # Velocidad promedio en km/h

    paradas = 0

    while viaje > 0:
        distancia_faltante = auto.andar(velocidad, 1)
        if distancia_faltante > 0:
            paradas += 1
            print(f"Necesitas detenerte para cargar combustible. Faltan recorrer {distancia_faltante} km.")
        viaje -= distancia_faltante

    print(f"Total de paradas requeridas: {paradas}")
