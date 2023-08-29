class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        self.nivel_estanque=self.nivel_estanque-(distancia/self.rendimiento)
        if self.nivel_estanque>=0:
            print (self.nivel_estanque)
            return 0
        else:
            distancia_restante=distancia-self.nivel_estanque*self.rendimiento
            return distancia_restante
    def autonomia(self):
        distancia=self.nivel_estanque*self.rendimiento
        return distancia
    def llenar_estanque(self,cantidad_litros):
        if cantidad_litros<=self.capacidad_estanque-self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque+cantidad_litros
            return self.nivel_estanque
            return True
        else:
            max_combustible=self.capacidad_estanque-self.nivel_estanque
            return max_combustible
            return False

if __name__ == "__main__":
    auto=Auto(100,12)
         