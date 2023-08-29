class Auto:
    def __init__(self,v,r):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=v
        self.nivel_estanque=0
        self.rendimiento=r
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def autonomia(self):
        andable=self.nivel_estanque*self.rendimiento
        return andable
    def andar(self,vel,t):
        d=vel*t
        andable=self.autonomia()
        c=d/self.rendimiento
        if d<=andable:
            self.kilometraje+=d
            self.cuenta_kilometros+=d
            self.nivel_estanque-=c
            return 0
        else:
            self.kilometraje+=andable
            self.cuenta_kilometros+=andable
            self.nivel_estanque=0
            return andable-d
    def llenar_estanque(self,l):
        maximum=self.capacidad_estanque-self.nivel_estanque
        if l<=maximum:
            self.nivel_estanque+=l
            return self.nivel_estanque,True
        else:
            return maximum,False

if __name__=="__main__":
    auto=Auto(100,12)
    d=float(input("Ingrese el largo de su viaje, en kilómetros: "))
    veces=1
    auto.llenar_estanque(auto.capacidad_estanque)
    k=auto.autonomia()
    auto.nivel_estanque=0
    veces+=d//k
    print("Deberá recargar el estanque",int(veces),"veces")