__version__ = "1.0"

import time
import html

from multiprocessing import Queue,Process,TimeoutError

class GradingResult:
    def __init__(self):
        self.estado=False
        self.puntaje=0
        self.mensaje="<p>Por favor intenta nuevamente.</p>"

    def generar_error(self,mensaje,puntaje):
        self.estado=False
        self.puntaje=puntaje
        self.mensaje=mensaje

    def generar_exito(self,puntaje):
        self.estado=True
        self.puntaje=puntaje
        self.mensaje="<p><emph>Tu programa funciona correctamente, Buen Trabajo!</emph></p>"

class Grader:
    def __init__(self):
        self.inicio=time.strftime("%d/%m/%Y %H:%M:%S")
        self.correctas=[]
        self.incorrectas=[]

    def agregar(self,errores):
        for error in errores:
            self.logFalla(error)

    def logFalla(self,error):
        self.incorrectas.append("<td>ERROR</td><td>{0}</td>".format(html.escape(str(error),quote=True)))

    def logExito(self,prueba):
        self.correctas.append("<td>OK</td><td>{0}</td>".format(prueba))

    def generarMensaje(self):
        resultado="<table>"
        for correcta in self.correctas:
            resultado+="<tr>{0}</tr>".format(correcta)
        for incorrecta in self.incorrectas:
            resultado+="<tr>{0}</tr>".format(incorrecta)
        resultado+="</table>"
        return resultado

    def iniciar_revision(self,ejercicio,puntaje,fuente,funcion_revision):

        try:
            r=Queue()
            p=Process(target=funcion_revision,args=(ejercicio,fuente,r,))
            p.start()
            p.join(10)
            if p.is_alive():
                p.terminate()
                self.logFalla("Posible Loop Infinito en tu programa")
                errores=[]
                score=0
            else:
                errores=r.get(timeout=1)
                score=float(errores.pop())
            del p

            self.agregar(errores)

        except TimeoutError as timeout:
            self.logFalla("Posible Loop Infinito")
        except BaseException as e:
            self.logFalla(str(e))

        resultado=GradingResult()
        if len(self.incorrectas)==0:
            resultado.generar_exito(puntaje)
        else:
            mensaje=self.generarMensaje()
            resultado.generar_error(mensaje,puntaje*score)
        return resultado
