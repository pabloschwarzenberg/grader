class Auto:

    def __init__(self,capacidad_estanque,rendimiento):
        self.kilometraje=0
        self.capacidad_estanque=capacidad_estanque
        self.rendimiento=rendimiento
        self.cuenta_kilometros=0
        self.nivel_estanque=0

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros=0
        
    def andar(self,velocidad,tiempo):
        km=velocidad*tiempo
        self.cuenta_kilometros+=km
        self.kilometraje+=km
        L=km/self.rendimiento
        self.nivel_estanque-=L
        
        if self.nivel_estanque>=0:
            km_faltantes=0
        else:
            km_quealcanza=self.nivel_estanque*rendimiento
            km_faltantes=km-km_quealcanza
        print("kilometros que faltan",km_faltantes)


    def autonomia(self):
        km_rec=self.rendimiento*self.nivel_estanque
        return (km_rec)
        
    def llenar_estanque(self,litros):
        if litros<=100:
            self.nivel_estanque=litros
            lista=[litros,True]
        else:
            lista=["100",False]
        print(lista)

auto=Auto(100,12)
