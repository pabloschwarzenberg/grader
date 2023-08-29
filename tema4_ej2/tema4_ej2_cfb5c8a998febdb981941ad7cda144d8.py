class Auto:
    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento
    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0
    def andar(self,v,t):
        distancia = v * t
        litrosgastados = distancia / rendimiento
        self.nivel_estanque = self.nivel_estanque + litrosgastados
        self.kilometraje = self.kilometraje + distancia
        if self.cuenta_kilometros == 0:
            self.cuenta_kilometros = self.cuenta_kilometros + distancia
        if self.nivel_estanque >=0:
            return 0
        else:
            return (-self.nivel_estanque)* rendimiento
    def autonomia(self):
        a = self.rendimiento * self.nivel_estanque
        return a
    def llenar_estanque(self,litros):
        self.nivel_estanque = self.nivel_estanque + litros
        if self.nivel_estanque <= self.capacidad_estanque:
            return (self.nivel_estanque,True)
        else:
            return (self.capacidad_estanque,False)