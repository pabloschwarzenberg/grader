class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
    def andar(self,velocidad,tiempo):
        km=velocidad*tiempo
        self.kilometraje+=km
        self.cuenta_kilometros+=km
        L=km/self.rendimiento
        self.nivel_estanque-=L
    def autonomia(self):
        kilometros=int(self.nivel_estanque)*int(self.rendimiento)
        return kilometros
    def llenar_estanque(self,litros):
        if litros>self.capacidad_estanque:
            if litros+nivel_estanque>capacidad_estanque:
                nivel_estanque=nivel_estanque
                return False
        else:
            self.nivel_estanque+=litros
            return True

if __name__ == "__main__":
    auto=Auto(100,12)
         