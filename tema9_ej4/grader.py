__version__ = "1.0"
import analizador.util
import tema9_ej4.solucion
import tema9_ej4.plantilla

class Analizador(analizador.util.AnalizadorBase):
    def __init__(self):
        analizador.util.AnalizadorBase.__init__(self)

    def analizar(self):
        esperado=tema9_ej4.solucion.Usuario("pablo","phschwarzenberg@uc.cl")
        observado=self.modulo.Usuario("pablo","phschwarzenberg@uc.cl")
        e=esperado.cambiar_password("clave")
        o=observado.cambiar_password("clave")
        if e!=o:
            self.errores.append("Si password={0} el resultado debiera ser {1}".format("clave",e))

        e=esperado.cambiar_password("clavesecreta1_")
        o=observado.cambiar_password("clavesecreta1_")
        if e!=o:
            self.errores.append("Si password={0} el resultado debiera ser {1}".format("clavesecreta1_",e))

        e=esperado.cambiar_password("clavesecreta")
        o=observado.cambiar_password("clavesecreta")
        if e!=o:
            self.errores.append("Si password={0} el resultado debiera ser {1}".format("clavesecreta",e))

        e=esperado.cambiar_password("clavesecreta1")
        o=observado.cambiar_password("clavesecreta1")
        if e!=o:
            self.errores.append("Si password={0} el resultado debiera ser {1}".format("clavesecreta1",e))

        e=esperado.cambiar_password("claveSecreta1")
        o=observado.cambiar_password("claveSecreta1")
        if e!=o:
            self.errores.append("Si password={0} el resultado debiera ser {1}".format("claveSecreta1",e))

        e=esperado.login("clavesecreta1_")
        o=observado.login("clavesecreta1_")
        if e!=o:
            self.errores.append("Si password={0} al realizar login con {1} el resultado debiera ser {2}"
                                .format("claveSecreta1","clavesecreta1_",e))

if __name__=="__main__":
    analizador=Analizador()
    analizador.modulo=tema9_ej4.plantilla
    analizador.analizar()
    for error in analizador.errores:
        print(error)