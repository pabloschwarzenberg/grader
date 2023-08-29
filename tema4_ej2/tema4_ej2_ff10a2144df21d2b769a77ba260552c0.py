class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def llenar_estanque(self,cantidad_de_litros):
        if cantidad_de_litros<=self.capacidad_estanque:
            self.nivel_estanque=cantidad_de_litros
            tupla=(self.nivel_estanque,True)
            return tupla
        if cantidad_de_litros>self.capacidad_estanque:
            tupla=(self.capacidad_estanque,False)
            return tupla

    def autonomia(self):
        autonomia=self.rendimiento*self.nivel_estanque
        return autonomia

    def andar(self,velocidad,tiempo_de_viaje):
        distancia=velocidad*tiempo_de_viaje
        self.kilometraje=distancia
        self.cuenta_kilometros=distancia
        litros_necesarios=distancia/self.rendimiento
        if litros_necesarios<=self.nivel_estanque:
            self.nivel_estanque=self.nivel_estanque-litros_necesarios
            return 0
        if litros_necesarios>self.nivel_estanque:
            self.nivel_estanque=0
            distancia_recorrida=self.rendimiento*self.nivel_estanque
            distancia_que_falta=distancia-distancia_recorrida
            return distancia_que_falta
    
    

if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto.rendimiento)
    print(auto.nivel_estanque)



