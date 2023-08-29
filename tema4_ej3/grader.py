__version__ = "1.0"
import analizador.util
import tema4_ej3.solucion
import tema4_ej3.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        o=self.modulo.jerigonzo("estamos programando")
        e=tema4_ej3.solucion.jerigonzo("estamos programando")
        if o!=e:
            self.errores.append("Al codificar la frase 'estamos programando' tu funcion debiera retornar {0}".format(e))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema4_ej3.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)
