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
            faltante = litros_consumidos - self.nivel_estanque
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Ejemplo de uso del programa

auto = Auto(100, 12)  # Capacidad del estanque: 100 litros, Rendimiento: 12 km/l

velocidad = 60  # Velocidad en km/h
tiempo_viaje = 6  # Tiempo de viaje en horas

total_kilometros = velocidad * tiempo_viaje
viajes = 0

while total_kilometros > 0:
    faltante = auto.andar(velocidad, tiempo_viaje)
    
    if faltante > 0:
        viajes += 1
        litros_a_cargar, exito = auto.llenar_estanque(faltante)
        
        if exito:
            total_kilometros -= litros_a_cargar * auto.rendimiento
        else:
            print("No se puede completar el viaje. Necesitas un auto con mayor capacidad de estanque.")
            break
    else:
        total_kilometros -= velocidad * tiempo_viaje

print("Número de paradas necesarias para cargar combustible:", viajes)
