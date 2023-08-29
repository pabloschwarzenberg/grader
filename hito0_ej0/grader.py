import analizador.util
import io
import sys

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","plantilla.py")
    for error in analizador.errores:
        print(error)