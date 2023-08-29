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
        self.kilometraje+=velocidad*tiempo_viaje
        self.cuenta_kilometros+=velocidad*tiempo_viaje
        self.nivel_estanque-=velocidad*tiempo_viaje/self.rendimiento
        if self.nivel_estanque>=0:
            return 0
        elif self.nivel_estanque<0:
            kilometros_faltantes=velocidad*tiempo_viaje-((0-self.nivel_estanque)*self.rendimiento)
            self.nivel_estanque=0
            return  kilometros_faltantes
    def autonomia(self):
        autonomia=self.nivel_estanque*self.rendimiento
        return autonomia
    def llenar_estanque(self,cantidad_litros):
       litros=self.nivel_estanque+cantidad_litros
       if litros>self.capacidad_estanque:
            return self.capacidad_estanque,False
       else:
            self.nivel_estanque+=litros
            return self.nivel_estanque,True



if __name__ == "__main__":
    auto=Auto(100,12)
    distancia_a_recorrer=int(input("Ingrese distancia a recorres:"))
    distancia_a_recorrer=int(input("Ingrese tiempo a recorres:"))
    auto.llenar_estanque(100)
    a=auto.andar(distancia_a_recorrer,tiempo)
    if a==True:
        print(0)     
    else:
        b=auto.autonomia()/distancia_a_recorrer
        print(b)
         