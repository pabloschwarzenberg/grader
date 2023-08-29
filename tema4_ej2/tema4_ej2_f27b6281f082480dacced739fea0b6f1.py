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
            self.kilometraje += (distancia - kilometros_faltantes)
            self.cuenta_kilometros += (distancia - kilometros_faltantes)
            self.nivel_estanque = 0
            return kilometros_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += cantidad_litros
            return (self.nivel_estanque, True)
        else:
            litros_permitidos = self.capacidad_estanque - self.nivel_estanque
            return (litros_permitidos, False)


auto = Auto(100, 12)

velocidad_viaje = 60
tiempo_viaje = 4

distancia_viaje = velocidad_viaje * tiempo_viaje
litros_necesarios = distancia_viaje / auto.rendimiento
paradas_carga_combustible = int(litros_necesarios / auto.capacidad_estanque)

if litros_necesarios % auto.capacidad_estanque != 0:
    paradas_carga_combustible += 1

print("Número de paradas de carga de combustible:", paradas_carga_combustible) 