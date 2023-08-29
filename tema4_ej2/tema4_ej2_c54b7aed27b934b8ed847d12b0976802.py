class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
        pass

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return

    def autonomia(self):
        aut=self.rendimiento*self.nivel_estanque
        return aut

    def andar(self,velocidad,tiempo):
        distancia=velocidad*tiempo
        if distancia<=self.rendimiento*self.nivel_estanque:
            self.kilometraje=self.kilometraje+distancia
            gastado=distancia/self.rendimiento
            self.nivel_estanque=self.nivel_estanque-gastado
            self.cuenta_kilometros=self.cuenta_kilometros+distancia
            return 0
        else:
            restante=distancia- self.rendimiento*self.nivel_estanque
            return restante


    def llenar_estanque(self,cantidad):
        if cantidad+self.nivel_estanque >self.capacidad_estanque:
            maximo=self.capacidad_estanque-self.nivel_estanque
            return (maximo,False)
        elif cantidad+self.nivel_estanque <=self.capacidad_estanque:
            self.nivel_estanque=cantidad+self.nivel_estanque
            return (self.nivel_estanque,True)

if __name__ == "__main__":
    auto=Auto(100,12)
    distancia=int(input("ingrese el largo del viaje"))
    a=auto.capacidad_estanque*auto.rendimiento
    b=distancia//a
    print("necesita cargar combustible",b,"veces")
         