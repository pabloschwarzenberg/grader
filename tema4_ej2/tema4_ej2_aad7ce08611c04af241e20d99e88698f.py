class   Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.capacidad=capacidad_estanque
        self.rendimiento=rendimiento
    kilometraje=0
    cuenta_kilometros=0
    nivel_estanque=0
    def reiniciar_cuentakilometros(self):
        cuenta_kilometros=0
    def andar(self, velocidad, tiempo):
        distancia=velocidad*tiempo
        litros_usados=distancia/self.rendimiento
        if (self.nivel_estanque-litros_usados)<0:
            resto=litros_usados-self.nivel_estanque
            distancia_faltante=litros*self.rendimiento
            return distancia_faltante
        else:
            self.nivel_estanque=self.nivel_estanque-litros_usados
            self.kilometraje+=distancia
            self.cuenta_kilometros+=distancia
            return 0
    def autonomia(self):
        distancia=self.rendimiento*self.nivel_estanque
        return distancia
    def llenar_estanque(self, litros):
        faltante=self.capacidad-self.nivel_estanque
        if litros > faltante:
            return (faltante, False)
        else:
            self.nivel_estanque+=litros
            return(self.nivel_estanque, True)

if __name__ == "__main__":
    auto=Auto(100,12)
         