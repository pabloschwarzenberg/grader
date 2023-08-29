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
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= litros_consumidos
            return 0
        else:
            kilometros_faltantes = (litros_consumidos - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia - kilometros_faltantes
            self.cuenta_kilometros += distancia - kilometros_faltantes
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        litros_posibles = self.capacidad_estanque - self.nivel_estanque
        if cantidad_litros <= litros_posibles:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            return litros_posibles, False


# Ejemplo de uso
auto = Auto(100, 12)

viaje = [(100, 1), (80, 0.5), (60, 2), (120, 1)]

paradas_carga = 0

for velocidad, tiempo in viaje:
    kilometros_faltantes = auto.andar(velocidad, tiempo)
    if kilometros_faltantes > 0:
        paradas_carga += 1
        litros_necesarios = (kilometros_faltantes / auto.rendimiento) - auto.nivel_estanque
        litros_cargados, exito = auto.llenar_estanque(litros_necesarios)
        if not exito:
            print("No es posible completar el viaje.")
            break

print("Cantidad de paradas de carga necesarias:", paradas_carga)
