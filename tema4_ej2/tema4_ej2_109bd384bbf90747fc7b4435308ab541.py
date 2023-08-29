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
            distancia_restante = self.rendimiento * self.nivel_estanque
            self.kilometraje += distancia_restante
            self.cuenta_kilometros += distancia_restante
            self.nivel_estanque = 0
            return distancia - distancia_restante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return litros, True
        else:
            return self.capacidad_estanque, False


# Ejemplo de uso
auto = Auto(100, 12)

distancia_total = 800  # Distancia total del viaje
velocidad = 80  # Velocidad promedio en km/h

tiempo_total = distancia_total / velocidad  # Calcula el tiempo total del viaje

# Calcula cuántas veces debe detenerse a cargar combustible
detenciones = 0
while distancia_total > 0:
    distancia_recorrida = auto.andar(velocidad, tiempo_total)
    if distancia_recorrida > 0:
        detenciones += 1
        distancia_total -= distancia_recorrida
    else:
        break

print("Detenciones necesarias:", detenciones)
