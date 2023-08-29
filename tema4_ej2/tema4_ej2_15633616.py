class Auto:
    def __init__(self, capacidad_estanque, rendimiento, kilometraje=0, cuenta_kilometros=0, nivel_estanque=0):
        self.kilometraje=kilometraje
        self.cuenta_kilometros=cuenta_kilometros
        self.capacidad_estanque=capacidad_estanque
        self.nivel_estanque=nivel_estanque
        self.rendimiento=rendimiento
    def  reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        return str("El cuenta kilometros esta en: ",self.cuenta_kilometros)
    def andar(self, v, t):
        d=v*t
        self.kilometraje=self.kilometraje+d
        self.cuenta_kilometros= self.cuenta_kilometros+d
        self.nivel_estanque=self.nivel_estanque-(d/self.rendimiento)
        if self.nivel_estanque>0:
            return 0
        else:
            return d-((self.nivel_estanque+(d/self.rendimiento))*self.rendimiento)
        
    def autonomia(self):
        d=self.rendimiento*self.nivel_estanque
        return d
    def llenar_estanque(self, l):
        self.nivel_estanque=self.nivel_estanque+l
        if self.nivel_estanque>self.capacidad_estanque:
            self.nivel_estanque=self.nivel_estanque-l
            return self.capacidad_estanque-(self.nivel_estanque-l) and False
        else:
            return self.nivel_estanque and True
        
if __name__ == "__main__":
    auto=Auto(100,12)
    p=0
    d=eval(input("Distancia a recorrer: "))   
    while auto.cuenta_kilometros<d:
       auto.llenar_estanque(auto.capacidad_estanque-auto.nivel_estanque)
       p=p+1
       auto.cuenta_kilometros+=auto.autonomia()
    print("El auto se tendra que detener", p, "veces")