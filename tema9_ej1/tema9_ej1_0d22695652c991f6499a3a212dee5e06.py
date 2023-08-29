class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        #Convertir el mensaje en una lista de palabras
        p = mensaje.split()
        #Recorrer la lista de palabras y localizar los hashtags
        for l in p: #Para cada palabra en la lista
          if "#" in l: #Si la palabra es un hashtag
            if not l in self.trending_topics: #Si el hashtag no está en la lista
              #Se agrega el hashtag a la lista
              self.trending_topics.append(l)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)