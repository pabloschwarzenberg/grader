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
            faltante = distancia - self.nivel_estanque * self.rendimiento
            self.kilometraje += self.nivel_estanque * self.rendimiento
            self.cuenta_kilometros += self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            return faltante
    
    def autonomia(self):
        return self.nivel_estanque * self.rendimiento
    
    def llenar_estanque(self, cantidad_litros):
        if cantidad_litros > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque = cantidad_litros
            return self.nivel_estanque, True

auto = Auto(100, 12)
viaje_distancia = 500
viaje_tiempo = 5
paradas = 0

while viaje_distancia > 0:
    resultado = auto.andar(100, viaje_tiempo)
    if resultado > 0:
        paradas += 1
    viaje_distancia -= resultado

print("Cantidad de paradas requeridas:", paradas)
