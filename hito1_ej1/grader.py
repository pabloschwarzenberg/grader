import analizador.util
import io
import sys
import random

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)
        self.notas=[random.uniform(1,7),random.uniform(1,7),random.uniform(1,7),random.uniform(1,7)]

    def iniciar_redireccion(self):
        sys.stdin=io.StringIO()
        for nota in self.notas:
            sys.stdin.write("{0}\n".format(nota))
        sys.stdin.seek(0)
        sys.stdout=io.StringIO()

    def analizar(self):
        salida=sys.stdout.getvalue().strip()
        promedio_esperado=round(self.notas[0]*0.3+self.notas[1]*0.3+self.notas[2]*0.3+self.notas[3]*0.1,1)
        if salida.find(str(promedio_esperado))==-1:
            self.errores.append("El promedio de {0} debiera ser {1} no {2}".format(self.notas,
            promedio_esperado,salida))

if __name__=="__main__":
    analizador=Analizador()
    analizador.revisar(".","solucion.py")
    for error in analizador.errores:
        print(error)