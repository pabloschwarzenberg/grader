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
            km_faltantes = (litros_necesarios - self.nivel_estanque) * self.rendimiento
            self.kilometraje += (distancia - km_faltantes)
            self.cuenta_kilometros += (distancia - km_faltantes)
            self.nivel_estanque = 0
            return km_faltantes
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, litros):
        if self.nivel_estanque + litros <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return self.nivel_estanque, True
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return max_litros, False


# Programa principal
auto = Auto(capacidad_estanque=100, rendimiento=12)
viaje = [(80, 2), (60, 3), (70, 4)]  # Lista de tuplas: (velocidad, tiempo)

paradas = 0
for tramo in viaje:
    velocidad, tiempo = tramo
    resultado = auto.andar(velocidad, tiempo)
    if resultado > 0:
        paradas += 1

print("Tendrás que detenerte a cargar combustible", paradas, "veces en este viaje.")
