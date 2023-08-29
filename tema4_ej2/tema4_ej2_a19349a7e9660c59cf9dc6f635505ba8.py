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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False


# Programa principal
capacidad_estanque = 100
rendimiento = 12
auto = Auto(capacidad_estanque, rendimiento)

velocidad = 80  # Velocidad promedio en km/h
tiempo_viaje = 6  # Tiempo de viaje en horas

distancia_total = velocidad * tiempo_viaje
litros_necesarios_total = distancia_total / rendimiento

num_paradas = 0
while litros_necesarios_total > 0:
    if litros_necesarios_total <= capacidad_estanque:
        auto.llenar_estanque(litros_necesarios_total)
        litros_necesarios_total = 0
    else:
        auto.llenar_estanque(capacidad_estanque)
        litros_necesarios_total -= capacidad_estanque
        num_paradas += 1

print("Tendras que detenerte a cargar combustible", num_paradas, "veces durante el viaje.")
