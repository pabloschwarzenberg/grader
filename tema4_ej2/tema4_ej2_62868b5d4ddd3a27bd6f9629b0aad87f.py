class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = int(capacidad_estanque)
        self.nivel_estanque = 0
        self.rendimiento = int(rendimiento)
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self, velocidad, tiempo):
        distancia = int(velocidad)*int(tiempo)
        litros_ocupados = distancia/self.rendimiento
        self.kilometraje += distancia
        self.cuenta_kilometros += distancia
        if self.nivel_estanque >= litros_ocupados:
            self.nivel_estanque -= litros_ocupados
            return 0
        else:
            d = litros_ocupados-self.nivel_estanque
            k = d*self.rendimiento
            self.nivel_estanque = 0
            return k
    def autonomia(self):
        recorrido = self.nivel_estanque*self.rendimiento
        return recorrido
    def llenar_estanque(self, cantidad_litros):
        if int(cantidad_litros) + self.nivel_estanque <= self.capacidad_estanque:
            self.nivel_estanque += int(cantidad_litros)
            return(self.nivel_estanque, True)
        else:
            diferencia = self.capacidad_estanque - self.nivel_estanque
            return(diferencia, False)




if __name__ == "__main__":
    auto=Auto(100,12)
         