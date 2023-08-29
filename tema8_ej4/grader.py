__version__ = "1.0"
import analizador.util
import tema8_ej4.solucion
import tema8_ej4.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        palabras=["hola","camioneta","zorro"]
        for palabra in palabras:
            esperado=tema8_ej4.solucion.rot13(palabra)
            observado=self.modulo.rot13(palabra)
            if esperado!=observado:
                self.errores.append("Al encriptar {0} el resultado debiera ser {1}".format(palabra,esperado))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema8_ej4.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)