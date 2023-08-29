import math

class Ciudad:
    def __init__(self,inicio,fin):
        self.inicio=int(inicio)
        self.fin=int(fin)

    def camino(p2):
        p2 = Ciudad(inicio2,fin2)
        diferencia_inicio=math.fabs(self.inicio-inicio2)
        diferencia_fin=math.fabs(self.fin-fin2)
        lista=[]
        if self.inicio>inicio2:
            if self.fin>fin2:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio += 1
                for i in range(1,diferencia_fin+1):
                    self.fin += 1
                    lista.append([self.inicio,self.fin])
            elif fin2 > self.fin:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio += 1
                for i in range(1,diferencia_fin+1):
                    self.fin -= self.fin
                    lista.append([self,inicio,self.fin])
            elif self.fin==fin2:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio += 1
        elif inicio2 > self.inicio:
            if self.fin>fin2:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio -= 1
                for i in range(1,diferencia_fin+1):
                    self.fin += 1
                    lista.append([self.inicio,self.fin])
            elif fin2 > self.fin:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio -= 1
                for i in range(1,diferencia_fin+1):
                    self.fin -= self.fin
                    lista.append([self,inicio,self.fin])
            elif self.fin==fin2:
                for i in range(1,diferencia_inicio+1):
                    lista.append([self.inicio,self.fin])
                    self.inicio -= 1
        elif inicio2 == self.inicio:
            if self.fin>fin2:
                for i in range(1,diferencia_fin+1):
                    self.fin += 1
                    lista.append([self.inicio,self.fin])
            elif fin2 > self.fin:
                for i in range(1,diferencia_fin+1):
                    self.fin -= self.fin
                    lista.append([self,inicio,self.fin])
        return lista
    def distancia(p2):
        p2 = Ciudad(inicio2,fin2)
        diferencia_inicio=math.fabs(self.inicio-inicio2)
        diferencia_fin=math.fabs(self.fin-fin2)
        cuadrados=int((diferencia_inicio**2)+diferencia_fin**2)
        raiz=float(math.sqrt(cuadrados))
        raiz=round(raiz,2)
        return raiz