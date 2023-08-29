#Clase Auto
class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return self.cuenta_kilometros
    def andar(self,velocidad,tiempo):
        self.kilometraje+=velocidad*(tiempo)
        self.cuenta_kilometros+=0
        self.nivel_estanque-=(velocidad*(tiempo))/self.rendimiento
        if self.nivel_estanque>=0:
            return 0
        else:
            return abs(self.nivel_estanque)*self.rendimiento
    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self,litros):
        if (litros+self.nivel_estanque)>self.capacidad_estanque:
            return self.capacidad_estanque,False
        else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True

if __name__ == "__main__":
    auto=Auto(100,12)