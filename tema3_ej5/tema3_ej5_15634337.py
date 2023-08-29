class Ciudad:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def camino(self,other):
        lista=[]
        pendiente=(self.b-other.b)/(self.a-other.a)
        contador=1
        a_prima=self.a
        b_prima=self.b
        lista2=[a_prima,b_prima]
        lista.append(lista2)
        while a_prima  < other.a:
            a_prima=self.a+contador
            b_prima=self.b+(pendiente*contador)
            contador+=1
            lista2=[a_prima,b_prima]
            lista.append(lista2)
        return lista
    def distancia(self,other):
        dist=(((self.a-other.a)**2)+((self.b-other.b)**2))**(1/2)
        return dist

if __name__ == "__main__":
  pass
         