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
        distancia_recorrida = velocidad * tiempo
        litros_necesarios = distancia_recorrida / self.rendimiento
        
        if litros_necesarios <= self.nivel_estanque:
            self.nivel_estanque -= litros_necesarios
            self.kilometraje += distancia_recorrida
            self.cuenta_kilometros += distancia_recorrida
            return 0
        else:
            kilometros_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += (distancia_recorrida - kilometros_faltantes)
            self.cuenta_kilometros += (distancia_recorrida - kilometros_faltantes)
            self.nivel_estanque = 0
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True


# Ejemplo de uso
auto = Auto(100, 12)

velocidad_viaje = 80  # km/h
tiempo_viaje = 4  # horas

distancia_total = velocidad_viaje * tiempo_viaje
litros_necesarios_total = distancia_total / auto.rendimiento

num_paradas = 0

while litros_necesarios_total > 0:
    litros_restantes, exito = auto.llenar_estanque(auto.capacidad_estanque)
    
    if exito:
        num_paradas += 1
        litros_necesarios_total -= litros_restantes
    else:
        break

print("Número de paradas necesarias:", num_paradas)
