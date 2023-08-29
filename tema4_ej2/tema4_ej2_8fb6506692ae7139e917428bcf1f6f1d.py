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
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

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

    distancia_viaje = float(input("Ingresa la distancia del viaje en kilómetros: "))
    velocidad_viaje = float(input("Ingresa la velocidad promedio del viaje en km/h: "))

    tiempo_viaje = distancia_viaje / velocidad_viaje
    cantidad_paradas = 0

    while distancia_viaje > 0:
        distancia_faltante = auto.andar(velocidad_viaje, tiempo_viaje)
        if distancia_faltante == 0:
            break
        cantidad_paradas += 1
        tiempo_viaje = distancia_faltante / velocidad_viaje

    print("Cantidad de paradas necesarias:", cantidad_paradas)
