class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        mensaje1=mensaje
        lista=mensaje.split(" ")
        lista_conrepetir=[]
        lista_sinrepetir=[]
        contador=[]
        if len(mensaje)<=140:
            for i in range(len(lista)):
                if lista[i][0]=="#":
                    lista_conrepetir.append(lista[i])
        for topics in lista_conrepetir:
            if topics not in self.trending_topics:
                self.trending_topics.append(topics)
                
        pass
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           