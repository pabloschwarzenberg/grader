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
            self.kilometraje += distancia - distancia_faltante
            self.cuenta_kilometros += distancia - distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True


# Ejemplo de uso
auto = Auto(100, 12)  # Crear un auto con estanque de 100 litros y rendimiento de 12 km/l

# Realizar un viaje
velocidad = 80  # km/h
tiempo = 6  # horas
distancia_viaje = velocidad * tiempo

# Calcular cuántas veces hay que detenerse a cargar combustible
num_paradas = 0
while distancia_viaje > 0:
    if auto.autonomia() < distancia_viaje:
        distancia_faltante = auto.andar(velocidad, tiempo)
        if distancia_faltante > 0:
            num_paradas += 1
        distancia_viaje -= distancia_faltante
    else:
        auto.andar(velocidad, tiempo)
        break

print("Número de paradas necesarias:", num_paradas)
