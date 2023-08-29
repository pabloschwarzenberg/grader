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
        litros=distancia/self.rendimiento
        self.kilometraje=self.kilometraje+distancia
        self.nivel_estanque=self.nivel_estanque-litros
        self.cuenta_kilometros=self.cuenta_kilometros+distancia
        if self.nivel_estanque<0:
            falto_distancia=self.nivel_estanque*-1*self.rendimiento
            return falto_distancia
        else:
            return 0

    def autonomia(self):
        puede_recorrer=self.nivel_estanque*self.rendimiento
        return puede_recorrer

    def llenar_estanque(self,cantidad_litros):
        suma=cantidad_litros+self.nivel_estanque
        if suma>self.capacidad_estanque:
            max_cantidad=self.capacidad_estanque-self.nivel_estanque
            tupla=(max_cantidad,False)
            return tupla
        else:
            self.nivel_estanque=suma
            tupla=(suma,True)
            return tupla
        
        
if __name__ == "__main__":
    auto = Auto(100, 12)
