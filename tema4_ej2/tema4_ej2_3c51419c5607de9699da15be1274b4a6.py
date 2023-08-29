class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuenta_kilometros(self):
        self.cuenta_kilometros = 0

    def andar(self,velocidad,tiempo):
        kilometrostotales = velocidad * tiempo
        kilometrosmaximos = self.nivel_estanque * self.rendimiento
        if kilometrostotales > kilometrosmaximos:
            kilometrosrestantes = kilometrostotales - kilometrosmaximos
            self.kilometraje += kilometrostotales - kilometrosrestantes
            self.cuenta_kilometros += kilometrostotales - kilometrosrestantes
            self.nivel_estanque = 0
            return kilometrosrestantes
        if kilometrostotales == kilometrosmaximos:
            self.kilometraje += kilometrostotales
            self.cuenta_kilometros += kilometrostotales
            self.nivel_estanque = 0
            return 0
        if kilometrosmaximos > kilometrostotales:
            kilometrossobra = kilometrosmaximos - kilometrostotales
            self.kilometraje += kilometrostotales
            self.cuenta_kilometros += kilometrostotales
            self.nivel_estanque = kilometrossobra / self.rendimiento
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self,litros):
        if litros + self.nivel_estanque > self.capacidad_estanque:
            return (self.capacidad_estanque, False)
        else:
            self.nivel_estanque += litros
            return (litros + self.nivel_estanque, True)
            
if __name__ == "__main__":
    auto = Auto(100,12)
    velocidad = int(input("Ingrese la velocidad: "))
    tiempo = int(input("Ingrese el tiempo de viaje: "))
    tiempo_original = tiempo
    c = 1
    while tiempo > 0:
        a = auto.andar(velocidad,tiempo)
        if a == 0:
            break
        if a != 0:
            auto.llenar_estanque(100)
            c += 1
            tiempo = int(a / velocidad)
    print("Para andar {0} km a un velocidad de {1} km/min, deberá llenar el estanque {2} veces.".format((velocidad * tiempo_original), velocidad, c))
