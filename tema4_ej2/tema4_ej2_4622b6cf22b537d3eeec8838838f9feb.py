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
            distancia_restante = self.nivel_estanque * self.rendimiento
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            self.nivel_estanque = 0
            return distancia - distancia_restante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_faltantes = self.capacidad_estanque - self.nivel_estanque

        if cantidad_litros <= litros_faltantes:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_faltantes, False


# Ejemplo de uso
auto = Auto(100, 12)  # Crear un auto con estanque de 100 litros y rendimiento de 12 km/l
distancia_total = 1000  # Distancia total del viaje en kilómetros
velocidad = 80  # Velocidad promedio en km/h
tiempo_viaje = distancia_total / velocidad  # Calcular el tiempo de viaje en horas

n_paradas = 0  # Contador de paradas para cargar combustible

while distancia_total > 0:
    distancia_faltante = auto.andar(velocidad, tiempo_viaje)
    if distancia_faltante > 0:
        n_paradas += 1
        cantidad_litros, _ = auto.llenar_estanque(auto.capacidad_estanque)
        distancia_total -= distancia_faltante
        tiempo_viaje = distancia_total / velocidad

print("Número de paradas necesarias:", n_paradas)
