class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuentakilometros=0
    def andar(self,velocidad,tiempo):
        km_recorridos=velocidad*tiempo
        self.cuenta_kilometros+=km_recorridos
        self.kilometraje+=km_recorridos
        litros=km_recorridos/self.rendimiento
        if(self.nivel_estanque>=litros):
            u=0
        else:
            u=litros-self.nivel_estanque
        self.nivel_estanque += -litros
        return(u)
    def autonomia(self):
        posibles=self.rendimiento*self.nivel_estanque
        return(posibles)
    def llenar_estanque(self,litros):
        litros_posibles=self.capacidad_estanque - self.nivel_estanque
        if(litros>litros_posibles):
            booleano=False
        else:
            self.nivel_estanque += litros
            booleano= True
        return(self.nivel_estanque,booleano)
    


if __name__ == "__main__":
    auto=Auto(100,12)
         