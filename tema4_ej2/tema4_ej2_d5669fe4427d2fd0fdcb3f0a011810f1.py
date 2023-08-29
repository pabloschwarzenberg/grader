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
            distancia_faltante = (self.nivel_estanque * self.rendimiento)
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia - distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Ejemplo de uso
auto = Auto(100, 12)
distancia_viaje = 500  # Distancia total del viaje en kilómetros
velocidad_viaje = 80  # Velocidad constante en km/h durante todo el viaje
tiempo_viaje = distancia_viaje / velocidad_viaje  # Tiempo en horas

n_paradas = 0  # Contador de paradas para cargar combustible

while distancia_viaje > 0:
    distancia_recorrida = auto.andar(velocidad_viaje, tiempo_viaje)
    if distancia_recorrida > 0:
        n_paradas += 1
        litros_necesarios = distancia_recorrida / auto.rendimiento
        litros_max, _ = auto.llenar_estanque(litros_necesarios)
        tiempo_viaje = distancia_recorrida / velocidad_viaje
    else:
        distancia_viaje = 0

print("Número de paradas para cargar combustible:", n_paradas)
