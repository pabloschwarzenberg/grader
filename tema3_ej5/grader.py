__version__ = "1.0"
import analizador.util
import tema3_ej5.solucion
import tema3_ej5.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        try:
            c1=self.modulo.Ciudad(1,1)
            c2=self.modulo.Ciudad(3,3)
        except TypeError:
            self.errores.append("Recuerda definir el constructor de la clase Ciudad")
            return
        ce1=tema3_ej5.solucion.Ciudad(1,1)
        ce2=tema3_ej5.solucion.Ciudad(3,3)
        camino=c1.camino(c2)
        if camino[0]!=[1,1] or camino[-1]!=[3,3]:
            self.errores.append("El camino desde (1,1) a (3,3) debe incluir a ambas ciudades")
        distancia=c1.distancia(c2)
        if distancia!=ce1.distancia(ce2):
            self.errores.append("La distancia entre (1,1) y (3,3) debe ser {0}".format(ce1.distancia(ce2)))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema3_ej5.solucion
    analizador.analizar()
    for error in analizador.errores:
        print(error)