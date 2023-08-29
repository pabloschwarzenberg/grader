class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        distancia = velocidad * tiempo
        consumo_combustible = distancia / self.rendimiento
        if consumo_combustible <= self.nivel_estanque:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= consumo_combustible
            return 0
        else:
            km_faltantes = (self.nivel_estanque * self.rendimiento) - self.cuenta_kilometros
            self.kilometraje += km_faltantes
            self.cuenta_kilometros += km_faltantes
            self.nivel_estanque = 0
            return km_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque:
            self.nivel_estanque = litros
            return self.nivel_estanque, True
        else:
            return self.capacidad_estanque, False

# Crear instancia del auto
mi_auto = Auto(capacidad_estanque=100, rendimiento=12)

# Definir las características del viaje
velocidad = 80  # km/h
tiempo_total = 10  # horas
distancia_total = velocidad * tiempo_total  # km

# Calcular la cantidad de paradas necesarias
paradas_necesarias = 0
distancia_recorrida = 0
while distancia_recorrida < distancia_total:
    km_faltantes = mi_auto.andar(velocidad, tiempo_total)
    if km_faltantes > 0:
        paradas_necesarias += 1
        litros_necesarios = km_faltantes / mi_auto.rendimiento
        mi_auto.llenar_estanque(litros_necesarios)
    else:
        distancia_recorrida += distancia_total

# Mostrar el resultado
print("Paradas necesarias:", paradas_necesarias)
