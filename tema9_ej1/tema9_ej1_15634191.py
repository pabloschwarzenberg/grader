import copy
class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.lista_tweets=[]

    def tweet(self,mensaje):
        self.trending_topics=[]
        if len(mensaje)>140:
            print("El tweet es demasiado largo. El numero maximo de caracteres es 140")
        else:
            cuenta=mensaje.count("#")
            if cuenta>0:
                mensaje=mensaje.split(" ")
                for i in mensaje:
                    if i.find("#")==0:
                        self.lista_tweets.append(i)
        lista=copy.copy(self.lista_tweets)
        for i in range(3):
            if lista!=[]:
                for i in lista:
                    max=0
                    if lista.count(i)>max:
                        trend=i
                for i in range(lista.count(trend)):
                    lista.remove(trend)
                self.trending_topics.append(trend)




if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)