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
            litros_faltantes = litros_necesarios - self.nivel_estanque
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return litros_faltantes

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


# Programa principal
auto = Auto(100, 12)  # Estanque de 100 litros y rendimiento de 12 km/l

# Datos del viaje
velocidad = int(input("Velocidad del viaje (km/h): "))
tiempo = int(input("Tiempo de viaje (horas): "))
distancia_viaje = velocidad * tiempo

litros_faltantes = 0
paradas = 0

while distancia_viaje > 0:
    litros_faltantes = auto.andar(velocidad, tiempo)
    if litros_faltantes > 0:
        paradas += 1
        litros, exito = auto.llenar_estanque(litros_faltantes)
        if not exito:
            print(f"No se pueden cargar {litros_faltantes} litros. Llenando con {litros} litros.")
        else:
            print(f"Llenando el estanque con {litros} litros.")

    distancia_viaje -= auto.cuenta_kilometros

print(f"Paradas necesarias: {paradas}")