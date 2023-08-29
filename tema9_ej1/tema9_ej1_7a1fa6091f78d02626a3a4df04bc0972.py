class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        # convertir el mensaje en una lista de palabras
        l = mensaje.split()
        # recorrer la lista de palabras y localizar los hashtags
        for p in l: # para cada palabra en la lista
          if "#" in p: # si la palabra es un hashtags
            if not p in self.trending_topics: # si el hashtags no está en la lista
              # se agrega el hashtags a la lista
              self.trending_topics.append(p)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           