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
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        litros_restantes = self.capacidad_estanque - self.nivel_estanque

        if litros <= litros_restantes:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            return litros_restantes, False


# Ejemplo de uso
auto = Auto(100, 12)

velocidad = 80
tiempo = 3
kilometros_recorridos = 0
paradas_combustible = 0

while kilometros_recorridos < 1000:
    distancia_faltante = auto.andar(velocidad, tiempo)
    kilometros_recorridos += distancia_faltante if distancia_faltante > 0 else velocidad * tiempo
    if distancia_faltante > 0:
        paradas_combustible += 1

print("Número de paradas de combustible necesarias:", paradas_combustible)

         