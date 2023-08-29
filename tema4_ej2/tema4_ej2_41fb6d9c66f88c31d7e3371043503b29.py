#no entiendo :(
class Auto:
    def __init__(self,capacidad_estanque, rendimiento):

        self.kilometraje = 0
        self.cuenta_kiometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento


    def reiniciar_cuentakilometros(self):
        self.cuenta_kiometros = 0

    def andar(self, velocidad, tiempo):
        dist = velocidad * tiempo
        if dist == auto.autonomia():
            self.cuenta_kiometros = dist
            self.nivel_estanque = 0
            return 0
        else:
            return (dist - auto.autonomia())

    def autonomia(self):
        return (self.rendimiento * self.nivel_estanque)

    def llenar_estanque(self, litros):
        if litros > (self.capacidad_estanque - self.nivel_estanque):
            tupla = ((self.capacidad_estanque - self.nivel_estanque), False)
            return tupla
        else:
            tuplaa = ((self.nivel_estanque + litros), True)
            return tuplaa

if __name__ == "__main__":
    auto = Auto(100,12)
         