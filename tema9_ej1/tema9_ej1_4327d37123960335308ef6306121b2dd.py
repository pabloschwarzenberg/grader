class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.gatos=[]

    def tweet(self,mensaje):
        tp=[]
        caracteres=len(mensaje)
        if caracteres<=140:
            mensaje=mensaje.split(' ')
            for palabra in mensaje:
                if palabra[0]=='#':
                    palabra=list(palabra)
                    palabra.pop(0)
                    palabra=''.join(palabra)
                    self.gatos.append(palabra)
        lista=[]
        for gato in self.gatos:
            contar=self.gatos.count(gato)
            l1=[gato,contar]
            lista.append(l1)
        lista.sort()
        i=0
        while i<len(lista)-1:
            if lista[i][0]==lista[i+1][0]:
                lista.pop(i)
                i=i
            else:
                i=i+1
       lista.sort(key=lambda x:x[1], reverse=True)
       if len(lista)>2:
           i=0
           while i<3:
               tp.append(lista[i])
               i=i+1
           
       if len(lista)==2:
           tp.append(lista[0])
           tp.append(lista[1])
      if len(lista)==1:
          tp.append(lista[0])
      self.trending_topics=tp
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           