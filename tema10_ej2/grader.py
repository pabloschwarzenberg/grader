__version__ = "1.0"
import analizador.util
import tema10_ej2.solucion
import tema10_ej2.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):

        p1=["gato","gallina","caro","jaron","Limon","jarron"]
        p2=["gatito","gallina","cara","jarron","limon","melon"]

        for i in range(6):
            e=tema10_ej2.solucion.levenshtein(p1[i],p2[i])
            o=self.modulo.levenshtein(p1[i],p2[i])
            if e!=o:
                self.errores.append("para {0} y {1} el resultado debiera ser {2}".format(p1[i],p2[i],e))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema10_ej2.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)