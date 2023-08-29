__version__ = "1.0"
import analizador.util
import tema9_ej1.solucion
import tema9_ej1.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        esperado=tema9_ej1.solucion.Twitter()
        esperado.tweet("gano #laroja")
        esperado.tweet("grande #chile")

        observado=self.modulo.Twitter()
        observado.tweet("gano #laroja")
        observado.tweet("grande #chile")

        if len(observado.trending_topics)!=len(esperado.trending_topics):
            self.errores.append("al twittear gano #laroja y luego grande #chile deberían haber {0} trending_topics"
                                .format(len(esperado.trending_topics)))

        esperado.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
        observado.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")

        if len(observado.trending_topics)!=len(esperado.trending_topics):
            self.errores.append("al continuar con #laroja con dos goles, le gano a brasil, grande #laroja deberían haber {0} trending_topics"
                                .format(len(esperado.trending_topics)))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema9_ej1.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)