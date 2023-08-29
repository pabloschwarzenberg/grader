class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) > 140:
            tweet = False
        else:
            tweet = True
            posLetra = 0
            mensaje = list(mensaje)
            for letra in mensaje:
                if letra == '#':
                    posEspacio = 0
                    for espacio in mensaje:
                        if espacio == ' ' and posEspacio > posLetra:
                            break
                        posEspacio += 1
                    hashtag = []
                    for i in range(posLetra,posEspacio):
                        hashtag.append(mensaje[i])
                    hashtag = ''.join(hashtag)
                    for trend in self.trending_topics:
                        if trend == hashtag:
                            print(trend)
                            self.trending_topics.remove(trend)
                            self.trending_topics.insert(0,trend)
                    if len(self.trending_topics) == 0 or self.trending_topics[0] != hashtag:
                        self.trending_topics.append(hashtag)
                posLetra +=1
            return tweet
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)