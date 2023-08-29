class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        # convertir en una lista el mensaje de entrada
        l = mensaje.split()
        # recorrer la lista y localizar los hashtags
        for p in l:
            if "#" in p: # si la palabra es un hashtag
                if not (p in self.trending_topics): # no se encuentra en la lista
                    # agregar el hashtag a la lista
                    self.trending_topics.append(p)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)