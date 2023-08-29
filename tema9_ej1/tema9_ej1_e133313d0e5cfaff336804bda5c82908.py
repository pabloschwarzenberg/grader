class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self,mensaje):
        self.mensaje = mensaje
        lista = mensaje.split(" ")
        hashtags = []
        if len(lista) < 140:
          for i in range(len(lista)):
            if lista[i][0] == "#":
              hashtags.append(lista[i])
        for topics in hashtags:
          if topics not in self.trending_topics:
            self.trending_topics.append(topics)
    
if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           