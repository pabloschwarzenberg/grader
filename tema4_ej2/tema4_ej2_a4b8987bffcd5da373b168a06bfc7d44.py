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
            distancia_recorrida = self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return distancia - distancia_recorrida

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)
auto = Auto(100, 12)
auto.llenar_estanque(100)
distancia_total = 1000
velocidad = 100
tiempo_total = distancia_total / velocidad
tiempo_por_viaje = auto.autonomia() / velocidad
num_paradas = 0

while tiempo_total > 0:
    if tiempo_total >= tiempo_por_viaje:
        auto.andar(velocidad, tiempo_por_viaje)
        tiempo_total -= tiempo_por_viaje
    else:
        auto.andar(velocidad, tiempo_total)
        tiempo_total = 0

    if auto.autonomia() == 0 and tiempo_total > 0:
        auto.llenar_estanque(100)
        num_paradas += 1

print("Número de paradas para cargar combustible:",num_paradas)
