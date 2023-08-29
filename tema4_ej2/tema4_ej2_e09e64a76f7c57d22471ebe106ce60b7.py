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
            distancia_faltante = self.rendimiento * self.nivel_estanque
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia - distancia_faltante

    def autonomia(self):
        return self.rendimiento * self.nivel_estanque

    def llenar_estanque(self, litros):
        if litros > self.capacidad_estanque - self.nivel_estanque:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            self.nivel_estanque = self.capacidad_estanque
            return (max_litros, False)
        else:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)


auto = Auto(100, 12)  # Crear instancia del auto con estanque de 100 litros y rendimiento de 12 km/l
viaje = 500  # Distancia total del viaje en kilómetros
velocidad = 60  # Velocidad promedio durante el viaje en km/h
tiempo_viaje = viaje / velocidad  # Calcular tiempo del viaje en horas
paradas = 0  # Inicializar contador de paradas

while viaje > 0:
    resultado = auto.andar(velocidad, tiempo_viaje)
    if resultado > 0:
        paradas += 1
        viaje = resultado
    else:
        viaje = 0

print("Tendrás que detenerte a cargar combustible", paradas, "veces durante el viaje.")

