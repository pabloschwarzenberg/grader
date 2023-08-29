import hito3_ej1.grader
import io
import sys
import random

class Analizador(hito3_ej1.grader.Analizador):
    def __init__(self):
        hito3_ej1.grader.Analizador.__init__(self)

    def analizar(self):
        hito3_ej1.grader.Analizador.analizar(self)
        try:
            grupo=self.modulo.Taxon("Clase","Aves")
        except Exception as e:
            return

        try:
            subcategorias=grupo.subcategorias

            n=len(subcategorias)

            if(n!=0):
                self.errores.append("subcategorias debe comenzar como lista de cero elementos")

        except Exception as e:
            if isinstance(e,AttributeError):
                self.errores.append("Recuerda inicializar el atributo subcategorias en __init__ usando self: "+str(e))
            elif isinstance(e,TypeError):
                self.errores.append("subcategorias debe comenzar como lista de cero elementos: "+str(e))

        return

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)