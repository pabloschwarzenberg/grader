class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        cantidad=mensaje.count("#")
        longitud=len(self.trending_topics)
        if longitud==0:
            s=int(mensaje.find("#"))
            hashtag=mensaje[s:]
            lista=[hashtag,cantidad]
            self.trending_topics.append(lista)
        else:
            if cantidad==1:
                s = int(mensaje.find("#"))
                hashtag = mensaje[s:]
                lista = [hashtag, cantidad]
                self.trending_topics.append(lista)
            else:
                s = int(mensaje.find("#"))
                fin=int(mensaje[s:].find(" "))
                hashtag=mensaje[s:fin]
                for i in range (longitud):
                    phashtag=self.trending_topics[i][0]
                    if phashtag==hashtag:
                        self.trending_topics[i][1]+=cantidad



if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           