__version__ = "1.0"
import analizador.util
import tema10_ej3.solucion
import tema10_ej3.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        e=tema10_ej3.solucion.sopaletras("/home/scheduler/grader/tema10_ej3/sopa.txt",["casa","cra","aro"])
        o=self.modulo.sopaletras("/home/scheduler/grader/tema10_ej3/sopa.txt",["casa","cra","aro"])
        for i in range(len(e)):
            encontrado=False
            for j in range(len(o)):
                if len(o[j])!=3:
                    self.errores.append("La función sopaletras debe retornar una tupla con 3 valores")
                    break
                if o[j][0]==e[i][0]:
                    encontrado=True
                    if o[j]!=e[i]:
                        self.errores.append("para {0} se espera {1}".format(o[j][0],e[i]))
            if not encontrado:
                self.errores.append("para {0} se espera {1}".format(e[i][0],e[i]))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema10_ej3.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)
