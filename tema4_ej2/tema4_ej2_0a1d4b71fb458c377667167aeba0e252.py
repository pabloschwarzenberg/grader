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
        consumo = distancia / self.rendimiento
        if consumo <= self.nivel_estanque:
            self.nivel_estanque -= consumo
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            return 0
        else:
            km_recorridos = self.nivel_estanque * self.rendimiento
            self.nivel_estanque = 0
            self.kilometraje += km_recorridos
            self.cuenta_kilometros += km_recorridos
            return distancia - km_recorridos

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        if litros + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += litros
            return (self.nivel_estanque, True)
        else:
            max_litros = self.capacidad_estanque - self.nivel_estanque
            return (max_litros, False)

def calcular_paradas(distancia, velocidad, tiempo_entre_paradas):
    auto = Auto(100, 12)
    paradas = 0
    while distancia > 0:
        auto.llenar_estanque(auto.capacidad_estanque)
        paradas += 1
        distancia_recorrida = auto.andar(velocidad, tiempo_entre_paradas)
        if distancia_recorrida == 0:
            distancia -= velocidad * tiempo_entre_paradas
        else:
            distancia -= distancia_recorrida
    return paradas - 1

print(calcular_paradas(1000, 100, 1))
