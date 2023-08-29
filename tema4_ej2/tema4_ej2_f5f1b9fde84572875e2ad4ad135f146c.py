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
        combustible_necesario = distancia / self.rendimiento

        if combustible_necesario > self.nivel_estanque:
            faltante = combustible_necesario - self.nivel_estanque
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
            self.nivel_estanque = 0
            return faltante
        else:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque -= combustible_necesario
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            cantidad_litros = self.capacidad_estanque

        self.nivel_estanque = cantidad_litros


# Ejemplo de uso
auto = Auto(100, 12)  # Crear un auto con estanque de 100 litros y rendimiento de 12 km/l

print("Autonomía:", auto.autonomia())  # Debe imprimir 0, ya que el estanque está vacío

auto.llenar_estanque(60)  # Llenar el estanque con 60 litros
print("Autonomía:", auto.autonomia())  # Debe imprimir 720, ya que 60 litros * 12 km/l = 720 km

tiempo_viaje = 1  # hora
velocidad = 120  # km/h

combustible_faltante = auto.andar(velocidad, tiempo_viaje)
print("Combustible faltante:", combustible_faltante)  # Debe imprimir 10.0, ya que 120 km / 12 km/l = 10 litros
print("Nivel de estanque:", auto.nivel_estanque)  # Debe imprimir 50.0, ya que 60 litros - 10 litros = 50 litros

         