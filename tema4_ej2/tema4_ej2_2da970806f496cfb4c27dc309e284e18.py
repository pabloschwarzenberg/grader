class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,v,t):
        d=v*t
        self.kilometraje=self.kilometraje+d
        self.cuenta_kilometros=self.cuenta_kilometros+d
        if self.nivel_estanque<(d/self.rendimiento):
            return (d-self.nivel_estanque*self.rendimiento)
        else:
            self.nivel_estanque=self.nivel_estanque-(d/self.rendimiento)
            return 0
    def autonomia(self):
        return self.rendimiento*self.nivel_estanque
    def llenar_estanque(self,litros):
        self.nivel_estanque=self.nivel_estanque+litros
        if self.nivel_estanque>self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque-litros
            return (self.capacidad_estanque, False)
        else:
            return (self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
    litros=int(input("cuantos litors desea recargar?"))
    while auto.llenar_estanque(litros)[1]==False:
        litros=int(input("la cantidad solicitada excede la capacidad del estanque,disminuya la cantidad:"))
    v=int(input("a que velocidad desea viajar:"))
    t=int(input("seleccione el tiempo de viaje:"))
    b=auto.autonomia()
    c=auto.andar(v,t)
    x=str((t*v)/b)
    if b>t*v:
        print("debe detenerse 1 vez a echar vencina")
    elif "0." not in x:
        pos=x.find(".")
        detenerse=x[0:pos]
        detenerse=int(detenerse)+1
        print("debe detenerse, ",detenerse," a echar bencina para llegar al destino" )
    else:
        print("debe detenerse,",x," veces para completar el viaje.")
    
         