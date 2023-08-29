import hito3_ej2.grader
import io
import sys
import random

class Analizador(hito3_ej2.grader.Analizador):
    def __init__(self):
        hito3_ej2.grader.Analizador.__init__(self)

    def analizar(self):
        hito3_ej2.grader.Analizador.analizar(self)
        try:
            grupo=self.modulo.Taxon("Clase","Aves")
            grupo2=self.modulo.Taxon("Orden","Falconiformes")
        except Exception as e:
            return

        try:
            grupo.incluir(grupo2)

        except Exception as e:
            if isinstance(e,AttributeError):
                self.errores.append("Recuerda definir el método incluir en la clase Taxon")
            if isinstance(e,TypeError):
                self.errores.append("Recuerda que el método incluir debe tener un parámetro además de self: "+str(e))

        if len(grupo.subcategorias)!=1:
            self.errores.append("El método incluir debe agregar un elemento al atributo subcategorias")
            return

        c=grupo.subcategorias[0]
        if not isinstance(c,self.modulo.Taxon):
            self.errores.append("Dentro de subcategorias debe haber un objeto de la clase Taxon")

        return

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)