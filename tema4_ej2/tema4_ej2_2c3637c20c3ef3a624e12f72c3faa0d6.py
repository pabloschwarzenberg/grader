class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.km = 0
        self.cuenta = 0
        self.r = rendimiento
        self.n = 0
        self.c = capacidad_estanque
    def reiniciar_cuentakilometros(self):
        self.c = 0
    def andar(self, velocidad, tiempoViaje):
        self.v = velocidad
        self.t = tiempoViaje
        self.n = self.r * self.t
        return self.n
        