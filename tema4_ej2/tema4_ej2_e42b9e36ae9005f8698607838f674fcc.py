class Auto:
    def __init__(self, capacidad_estanque, rendimiento):
        self.kilometraje = 0
        self.cuenta_kilometros = 0
        self.capacidad_estanque = capacidad_estanque
        self.nivel_estanque = 0
        self.rendimiento = rendimiento

    def reiniciar_cuentakilometros(self):
        self.cuenta_kilometros = 0

    def andar(self, velocidad, tiempo):
        camino_planeado = velocidad * tiempo
        bencina_necesaria = camino_planeado / self.rendimiento
        camino_maximo = self.nivel_estanque * self.rendimiento
        if bencina_necesaria > self.nivel_estanque:
            self.cuenta_kilometros += camino_maximo
            self.nivel_estanque = 0
            self.kilometraje += camino_maximo
            return (velocidad * tiempo) - camino_maximo
        else:
            self.cuenta_kilometros += camino_planeado
            self.nivel_estanque -= bencina_necesaria
            self.kilometraje += camino_planeado
            return 0

    def autonomia(self):
        return self.nivel_estanque * self.rendimiento

    def llenar_estanque(self, litros):
        maximo = self.capacidad_estanque - self.nivel_estanque
        if litros > maximo:
            return maximo, False
        else:
            nuevo_nivel = self.nivel_estanque + litros
            self.nivel_estanque += litros
            return nuevo_nivel, True


if __name__ == "__main__":
    auto = Auto(100, 12)
    camino = int(input('Ingresa la longitud del camino que quieres recorrer.'))
    print('¡Vamos a hacer andar el auto! BRRRRM BRRRRRRRRRRRRRRRRM')
    rapidez_media = int(input('¿A qué rapidez media (en km/s) irás durante el viaje?'))
    tiempo_estimado = camino / rapidez_media
    print('¡PARTIMOS! Vamos de paseo, pi, pi, pi, en un auto feo, ᴨ, ᴨ, ᴨ... (8)')
    resto = auto.andar(rapidez_media, tiempo_estimado)
    detenciones = 0
    while resto > 0:
        detenciones += 1
        print('¡OH NO! ¡SE ACABÓ LA MALDITA GASOLINAAAAAAAAAAAA! ¡AAAAAHHHHHHHHH!')
        print('Vamos a detenernos... ' + str(detenciones) + 'ª vez.')
    print('En total, se recorren ' + str(camino) + ' kilómetros con ' + str(detenciones) + ' detenciones.')
