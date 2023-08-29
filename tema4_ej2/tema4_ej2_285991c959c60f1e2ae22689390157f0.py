
class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo_viaje):
        distancia=velocidad*tiempo_viaje
        self.cuenta_kilometros+=distancia
        self.kilometraje+=distancia
        litros_gastados=distancia/self.rendimiento
        print("litros_gastados;"+str(litros_gastados))
        self.nivel_estanque-=litros_gastados
        print("nivel_estanque:"+str(self.nivel_estanque))
        if self.nivel_estanque >= 0:
            return 0
        else:
            return -(self.nivel_estanque)
    def autonomia(self):
        kill=self.rendimiento*self.nivel_estanque
        print("autonomia;"+str(kill))
        return kill

    def llenar_estanque(self,cantidad_de_litros):
        if self.nivel_estanque+cantidad_de_litros>self.capacidad_estanque:
            return (self.capacidad_estanque-self.nivel_estanque,False)
        else:
            self.nivel_estanque+=cantidad_de_litros
            return (self.nivel_estanque,True)
            
        
if __name__ == "__main__":
    auto=Auto(100,12)
    print(auto.llenar_estanque(60))
    print(auto.andar(50,30))
