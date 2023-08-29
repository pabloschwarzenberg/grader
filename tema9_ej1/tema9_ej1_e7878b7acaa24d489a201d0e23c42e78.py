class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.lista=[]

    def tweet(self,mensaje):
        lista2=[]
        mensaje=mensaje.split()
        for i in range(len(mensaje)):
            if "#" in mensaje[i]:
                self.lista.append(mensaje[i])
        lista1=list(set(self.lista))
        
        for k in range(len(lista1)):
            nro=self.lista.count(lista1[k])
            lista2.append(nro)
        for j in range(len(lista1)):   
            self.trending_topics.append(lista1[j])
        self.trending_topics=list(set(self.trending_topics))
               
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           