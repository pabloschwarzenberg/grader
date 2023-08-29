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
            faltante = litros_necesarios - self.nivel_estanque
            self.kilometraje += (self.nivel_estanque * self.rendimiento)
            self.cuenta_kilometros += (self.nivel_estanque * self.rendimiento)
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


# Ejemplo de uso
auto = Auto(100, 12)  # Estanque de 100 litros y rendimiento de 12 km/l

# Realizar el viaje
velocidad = 80  # km/h
tiempo = 6  # horas
viaje_completo = False
detenciones = 0

while not viaje_completo:
    faltante = auto.andar(velocidad, tiempo)
    if faltante == 0:
        viaje_completo = True
    else:
        detenciones += 1
        litros_a_cargar, _ = auto.llenar_estanque(faltante)
        print(f"Detención {detenciones}: Cargar {litros_a_cargar} litros")

print(f"Se realizaron {detenciones} detenciones para completar el viaje.")
