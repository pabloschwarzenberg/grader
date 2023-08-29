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
        litros_consumidos = distancia / self.rendimiento
        if litros_consumidos <= self.nivel_estanque:
            self.nivel_estanque -= litros_consumidos
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            faltante = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += distancia - faltante
            self.cuenta_kilometros += distancia - faltante
            return faltante

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
viaje = 1000  # Distancia del viaje en kilómetros
litros_por_parada = 50  # Cantidad de litros que puedes cargar en cada parada

paradas = 0

while viaje > 0:
    faltante = auto.andar(100, 1)  # Suponemos una velocidad constante de 100 km/h durante 1 hora
    if faltante > 0:
        paradas += 1
        litros_disponibles, _ = auto.llenar_estanque(litros_por_parada)
        if litros_disponibles < faltante:
            break
    viaje -= 100

print("Tendrás que detenerte a cargar combustible", paradas, "veces en el viaje.")
