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
            kilometros_faltantes = (self.nivel_estanque * self.rendimiento) - distancia
            self.kilometraje += (distancia - kilometros_faltantes)
            self.cuenta_kilometros += (distancia - kilometros_faltantes)
            self.nivel_estanque = 0
            return kilometros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque = min(self.capacidad_estanque, cantidad_litros)
            return self.nivel_estanque, True


# Uso de la clase Auto para determinar cuántas veces se debe cargar combustible en un viaje determinado
estanque_capacidad = 100
rendimiento_auto = 12

mi_auto = Auto(estanque_capacidad, rendimiento_auto)

# Llenar el estanque con 120 litros (superando la capacidad máxima)
litros_max, exito = mi_auto.llenar_estanque(120)
if not exito:
    print("ERROR: No se puede llenar el estanque con más litros de la capacidad máxima ({} litros)".format(estanque_capacidad))

# Verificar autonomía con 60 litros en el estanque
mi_auto.llenar_estanque(60)
autonomia = mi_auto.autonomia()
if autonomia != 720:
    print("ERROR: La autonomía esperada era de 720 km, pero se obtuvo: {} km".format(autonomia))

# Viajar 1 hora a 120 km/h
velocidad_viaje = 120
tiempo_viaje = 1
mi_auto.llenar_estanque(60)  # Reiniciar el estanque a 60 litros
resultado_viaje = mi_auto.andar(velocidad_viaje, tiempo_viaje)

if mi_auto.nivel_estanque != 50.0:
    print("ERROR: Después de viajar 1 hora a 120 km/h, el estanque debiera quedar con 50.0 litros, pero se obtuvo: {} litros".format(mi_auto.nivel_estanque))

print("Pruebas completadas.")