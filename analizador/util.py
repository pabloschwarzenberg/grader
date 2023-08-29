__version__ = "1.0"
import os
import sys
import inspect
import ast
import traceback

def cargarLocal(fuente):
    modulo=None
    nombre=None

    programa=list(filter(lambda x: x.startswith(fuente),os.listdir(".")))

    if len(programa)!=0:
        nombre=programa[0].split(".")[0]
        modulo=__import__(nombre, globals(), locals(), [nombre], 0)

    return nombre,modulo

def cargar(ejercicio,fuente):
    if ejercicio==".":
        resultado=cargarLocal(fuente)
        return resultado

    programa=list(filter(lambda x: x.startswith(fuente),os.listdir(ejercicio)))
    modulo=None
    nombre=None

    if len(programa)!=0:
        nombre=ejercicio+"."+programa[0].split(".")[0]
        modulo=__import__(nombre, globals(), locals(), [nombre], 0)

    return nombre,modulo

class AnalizadorBase:
    def __init__(self):
        self.modulo=None
        self.errores=[]
        self.score=0
        self.precondiciones=[self.iniciar_redireccion]
        self.revisiones=[self.analizar]

    def revisar(self,ejercicio,fuente,r=None):

        self.errores=[]
        self.score=0

        for i in range(len(self.revisiones)):

            self.precondiciones[i]()

            try:
                nombre,self.modulo=cargar(ejercicio,fuente)
                if self.modulo is None:
                    raise BaseException("No se encontro el programa a revisar")

                self.revisiones[i]()

                sys.modules.pop(nombre)

            except BaseException as e:
                traza = sys.exc_info()
                lineas = traceback.extract_tb(traza[2])
                lugar = lineas[-1]
                e=str(e)
                if (e.find("invalid syntax")==-1):
                    e="linea {0}: {1} -> {2}".format(lugar[1],lugar[3],e)
                self.errores.append(e)

            self.terminar_redireccion()

        self.errores.append(str(self.score))
        if r is not None:
            r.put(self.errores)

    def revisarUsoCiclos(self,funcion):
        fuente=inspect.getsource(funcion)
        raiz=ast.parse(fuente)
        encontrado=False
        for nodo in ast.walk(raiz):
            if isinstance(nodo,ast.While) or isinstance(nodo,ast.For):
                encontrado=True
        if(not encontrado):
            self.errores.append("Ciclos", "La función {0} no usa ciclos en su implementación".format(funcion.__name__))

    def revisarUsoFuncion(self,funcion,funcion_a_usar):
        fuente=inspect.getsource(funcion)
        raiz=ast.parse(fuente)
        encontrado=False
        for nodo in ast.walk(raiz):
            if isinstance(nodo,ast.Call):
                if "id" in nodo.func._fields:
                   if nodo.func.id==funcion_a_usar.__name__:
                        encontrado=True
        if(not encontrado):
            self.errores.append("Uso Función","La función {0} no usa a la función {1}".format(funcion.__name__,funcion_a_usar.__name__))

    def analizar(self):
        return

    def iniciar_redireccion(self):
        return

    def terminar_redireccion(self):
        sys.stdin=sys.__stdin__
        sys.stdout=sys.__stdout__
        sys.stderr=sys.__stderr__
