class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) < 140:
            for letra in mensaje:
                h_t = []
                if letra == "#":
                    posicion = mensaje.find("#")
                    hashtag = mensaje[posicion:]
                    h_t.append(hashtag)
                self.trending_topics.append(h_t)

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           