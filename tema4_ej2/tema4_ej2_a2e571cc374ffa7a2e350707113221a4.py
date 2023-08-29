class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, tiempo, velocidad):

        distancia = tiempo*velocidad
        distancia_max = self.nivel_estanque*self.rendimiento
        if distancia > distancia_max:
            falto = distancia-distancia_max
            return falto
        else:
            self.kilometraje += distancia
            self.cuenta_kilometros += distancia
            self.nivel_estanque = self.nivel_estanque - distancia/self.rendimiento
            self.nivel_estanque = float(self.nivel_estanque)
            return "0"

    def autonomia(self):
        return self.nivel_estanque*self.rendimiento

    def llenar_estanque(self, litros):
        if litros+self.nivel_estanque > self.capacidad_estanque:
            return self.capacidad_estanque, False
        else:
            self.nivel_estanque += litros
            return self.nivel_estanque, True


    def viaje(self, distancia):
        return distancia/(self.capacidad_estanque*self.rendimiento)



if __name__ == "__main__":
    auto = Auto(100, 12)
    auto.nivel_estanque = 60
    print(auto.andar(1, 120))
    print(auto.nivel_estanque)