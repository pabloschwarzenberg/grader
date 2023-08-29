class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        lista_hashtag=[]
        if len(mensaje) < 141:
            list = mensaje.split()
            for hashtag in list:
                if hashtag[0] == "#":
                    n = 0
                    for elemento in lista_hashtag:
                        if hashtag == elemento:
                            n = 1
                            v = lista_hashtag.index(elemento)
                    if n == 0:
                        lista_hashtag.append(hashtag+" 1")
                    else:
                        lista_hashtag.append(hashtag
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           