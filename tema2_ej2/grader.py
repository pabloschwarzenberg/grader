__version__ = "1.0"
import analizador.util

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        r1=self.modulo.amigos(1,2)
        if r1!=False:
            self.errores.append("El 1 y el 2 no son números amigos, pero tu función retorna {0}".format(r1))

        r1=self.modulo.amigos(4,4)
        if r1!=False:
            self.errores.append("El 4 y el 4 no son números amigos, pero tu función retorna {0}".format(r1))

        r1=self.modulo.amigos(220,284)
        if r1!=True:
            self.errores.append("El 220 y el 284 son números amigos y tu función retorna {0}".format(r1))

        r1=self.modulo.amigos(1184,1210)
        if r1!=True:
            self.errores.append("El 1184 y el 1210 son números amigos y tu función retorna {0}".format(r1))