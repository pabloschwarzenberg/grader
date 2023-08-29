import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        try:
            grupo=self.modulo.Taxon("Clase","Aves")
        except Exception as e:
            if isinstance(e,AttributeError):
                self.errores.append("Recuerda que debes crear la clase Taxon")
            elif isinstance(e,TypeError):
                self.errores.append("Recuerda que debes definir __init__ con dos parámetros: "+str(e))
            else:
                self.errores.append(str(e))

        try:
            nombre=grupo.nombre
            categoria=grupo.categoria
            if nombre!="Aves":
                self.errores.append("Al crear la Clase Aves, el nombre debiera ser {0} pero es {1}".format("Aves",nombre))

            if categoria!="Clase":
                self.errores.append("Al crear la Clase Aves, la categoria debiera ser {0} pero es {1}".format("Clase",categoria))

        except Exception as e:
            if isinstance(e,AttributeError):
                mensaje=str(e)
                if(mensaje.find("nombre")!=-1):
                    self.errores.append("Recuerda inicializar el atributo nombre en __init__ usando self: "+str(e))
                if(mensaje.find("categoria")!=-1):
                    self.errores.append("Recuerda inicializar el atributo categoria en __init__ usando self: "+str(e))
            else:
                self.errores.append(str(e))
        return

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)