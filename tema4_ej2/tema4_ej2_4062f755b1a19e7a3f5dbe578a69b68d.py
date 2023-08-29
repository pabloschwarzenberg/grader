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
        nuevo_kilometraje = self.kilometraje + (velocidad*tiempo)
        self.kilometraje = nuevo_kilometraje
        nuevo_litros = self.nivel_estanque - ((velocidad*tiempo)/self.rendimiento)
        self.nivel_estanque = nuevo_litros
        nuevo_cuenta_kilometros = self.cuenta_kilometros + (velocidad*tiempo)
        self.cuenta_kilometros = nuevo_cuenta_kilometros


    def autonomia(self):
        a = self.rendimiento * self.nivel_estanque
        return a
        

    def llenar_estanque(self, litros):
        estanque = self.nivel_estanque + litros
        if estanque > self.capacidad_estanque:
            print(self.capacidad_estanque)
            return False
        else:
            self.nivel_estanque = estanque
            print(estanque)
            return True

if __name__ == "__main__":
    auto=Auto(100,12)
         