class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.mensajes= []

    def tweet(self, mensaje):
        i=0
        if len(mensaje)<140:
            mm=mensaje.split(" ")
            i=0
            contador=0
            while i<len(mm):
                listaP=list(mm[i])
                if listaP[0]=="#":
                    contador+=1
                    listaS="".join(listaP)
                    self.trending_topics.append([listaS,contador])
                i=i+1
        print(sorted(self.trending_topics))


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           