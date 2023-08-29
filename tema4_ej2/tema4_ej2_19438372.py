class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0

    def andar(self,velocidad,tiempo):
        dist=velocidad*tiempo
        dist_max=self.nivel_estanque*self.rendimiento
        if dist>=dist_max:
            self.kilometraje+=dist_max
            self.cuenta_kilometros+=dist_max
            if dist==dist_max:
                self.nivel_estanque=0
            else:
                self.nivel=self.nivel_estanque-dist_max/self.rendimiento
            return 0
        else:
            self.kilometraje+=dist
            self.cuenta_kilometros+=dist
            self.nivel_estanque=self.nivel_estanque-dist/self.rendimiento
            falta=dist-dist_max
            return falta

    def autonomia(self):
        if self.nivel_estanque>0:
            a=self.nivel_estanque*self.rendimiento
            return a
        else:
            return 0

    def llenar_estanque(self,litros):
        if self.nivel_estanque+litros<=self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque+litros
        else:
            max=self.capacidad_estanque-self.nivel_estanque
            return (max,False)
if __name__ == "__main__":
    auto=Auto(100,12)
    print("El auto esta lleno")
    viaje=int(input("Ingrese la distancia a recorrer en el viaje"))
    auto.llenar_estanque(60)
    autonomia=auto.autonomia()
    resto=viaje%autonomia
    if autonomia>viaje or resto==0:
        n=0
    else:
        n=1
    veces=viaje//autonomia+n
    print(veces)

