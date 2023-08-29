class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.cuenta_kilometros=0
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=0
        self.rendimiento=rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
    def andar(self,velocidad,tiempo_viaje):
        self.nivel_estanque=self.nivel_estanque-(velocidad*tiempo_viaje)/self.rendimiento
        if self.nivel_estanque>=0:
            self.kilometraje+=(velocidad*tiempo_viaje)
            self.cuenta_kilometros+=(velocidad*tiempo_viaje)
            return 0
        elif self.nivel_estanque<0:
            self.kilometraje+=((velocidad*tiempo_viaje)+(self.nivel_estanque*self.rendimiento))
            self.cuenta_kilometros+=((velocidad*tiempo_viaje)+(self.nivel_estanque*self.rendimiento))                      
            return abs(self.nivel_estanque*self.rendimiento)
            
    def autonomia(self):
        return self.nivel_estanque*self.rendimiento
    def llenar_estanque(self, litros):
        false=[]
        true=[]
        if self.nivel_estanque+litros>self.capacidad_estanque:
            false=[self.capacidad_estanque-self.nivel_estanque, False]
            false=tuple(false)
            return false  #nombre de la tupla
        else:
            self.nivel_estanque+=litros
            true=[self.nivel_estanque, True]
            true=tuple(true)
            return true #nombre de la tupla


if __name__ == "__main__":         #100 litros     12 km/litro
    auto=Auto(100,12)
    print("Tu auto tiene estanque de 100 litros y rendimiento de 12km/litro")
    tiempo_viaje=float(input("Ingrese el tiempo de viaje en horas (formato decimal): "))
    velocidad=float(input("Ingrese velocidad del auto en el viaje en km/h: "))
    auto.llenar_estanque(100)
    e=auto.andar(velocidad,tiempo_viaje)
    conteo=0
    while e!=0:
        tiempo_viaje=((velocidad*tiempo_viaje)-auto.kilometraje)/velocidad
        auto.llenar_estanque(100)
        auto.reiniciar_cuentakilometros()
        conteo+=1
        e=auto.andar(velocidad,tiempo_viaje)
        if e==0:
            break
    print("Debes llenar",conteo,"veces el estanque.")
    print("estanque=",auto.nivel_estanque,"lts.")

