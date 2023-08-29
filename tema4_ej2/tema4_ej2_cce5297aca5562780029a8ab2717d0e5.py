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
            kilometros_faltantes = litros_necesarios * self.rendimiento
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros <= self.capacidad_estanque - self.nivel_estanque:
            self.nivel_estanque += cantidad_litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Ejemplo de uso
auto = Auto(100, 12)

velocidad = 60
tiempo = 2
faltante = auto.andar(velocidad, tiempo)
if faltante == 0:
    print("El viaje se completó sin problemas.")
else:
    print("No fue posible completar el viaje. Faltaron", faltante, "kilómetros por recorrer.")

num_paradas = 0
while faltante > 0:
    litros_necesarios = faltante / auto.rendimiento
    litros_disponibles, exito = auto.llenar_estanque(litros_necesarios)
    
    if not exito:
        break
    
    faltante = auto.andar(velocidad, tiempo)
    num_paradas += 1

print("Cantidad de paradas necesarias:", num_paradas)
