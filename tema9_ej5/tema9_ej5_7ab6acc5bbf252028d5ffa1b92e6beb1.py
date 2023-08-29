class JuegoDelGato:

    def __init__(self):
        fila=[[0,0,0],[0,0,0],[0,0,0]]
        pass

    def __repr__(self):
        return ""

    def jugarGato(self,fila,columna):
        if fila[fila[columna]]!=0:
            fila[fila[columna]]=1
            return True
        else:
            return False


    def jugarRaton(self):
        if self.fila[fila[columna]]!= 0:
            self.fila[fila[columna]]= -1
            return True
        pass

    def indicarEstado(self):
        pass

    def cargar_tablero(self,tablero):
        pass
