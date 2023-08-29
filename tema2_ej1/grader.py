__version__ = "1.0"
import analizador.util
import tema2_ej1.solucion
import tema2_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        ae1=tema2_ej1.solucion.area_triangulo(11,7)
        ae2=tema2_ej1.solucion.area_rectangulo(10,6)
        ae3=tema2_ej1.solucion.area_rombo(30,16)
        ae4=tema2_ej1.solucion.area_circulo(40)
        if ae1!=self.modulo.area_triangulo(11,7):
            self.errores.append("El area de un triangulo de base 11 y altura 7 debiera ser {0}".format(ae1))
        if ae2!=self.modulo.area_rectangulo(10,6):
            self.errores.append("El area de un rectangulo de lados 10 y 6 debiera ser {0}".format(ae2))
        if ae3!=self.modulo.area_rombo(30,16):
            self.errores.append("El area de un rombo con diagonales 30 y 16 debiera ser {0}".format(ae3))
        if ae4!=self.modulo.area_circulo(40):
            self.errores.append("El area de un círculo de radio 40 debiera ser {0}".format(ae4))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema2_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)