class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]

    def tweet(self,mensaje):
        Seba=[]
        mensaje=mensaje.split(" ")
        for i in mensaje:
           if i[0]=="#":
             i=list(i)
             i.pop(0)
             i="".join(i)
             self.hashtags.append(i)
        lista=[]
        for x in self.hashtags:
          contar=self.hashtags.count(x)
          a=[x,contar]
          lista.append(a)
        lista.sort()
        lista_nueva=[]
        for z in lista:
            if z not in lista_nueva:
                lista_nueva.append(z)
        lista_nueva.sort(key=lambda x:x[1], reverse = True)
        if len(lista_nueva) > 2:
            Seba.append(lista_nueva[0])
            Seba.append(lista_nueva[1])
            Seba.append(lista_nueva[2])
        if len(lista_nueva) == 2:
            Seba.append(lista_nueva[0])
            Seba.append(lista_nueva[1])
        if len(lista_nueva) ==1:
            Seba.append(lista_nueva[0])
        self.trending_topics=Seba
  