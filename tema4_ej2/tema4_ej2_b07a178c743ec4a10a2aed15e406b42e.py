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
            distancia_faltante = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += distancia_faltante
            self.cuenta_kilometros += distancia_faltante
            self.nivel_estanque = 0
            return distancia_faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            litros_maximos = self.capacidad_estanque - self.nivel_estanque
            return litros_maximos, False


# Ejemplo de uso
auto = Auto(capacidad_estanque=100, rendimiento=12)

velocidad = 80  # km/h
tiempo = 4  # horas

distancia_viaje = velocidad * tiempo
litros_necesarios = distancia_viaje / auto.rendimiento

num_paradas = 0
while litros_necesarios > 0:
    autonomia_actual = auto.autonomia()
    
    if litros_necesarios <= autonomia_actual:
        auto.andar(velocidad, tiempo)
        break
    
    litros_maximos, _ = auto.llenar_estanque(auto.capacidad_estanque)
    litros_necesarios -= litros_maximos
    num_paradas += 1

print("Número de paradas necesarias:", num_paradas)
         