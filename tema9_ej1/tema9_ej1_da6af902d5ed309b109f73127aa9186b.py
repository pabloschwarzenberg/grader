class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      if len(mensaje) <= 140:
        for palabra in mensaje.split(" "):
          if palabra.find("#")>=0:
            if not palabra in self.trending_topics:
              self.trending_topics.append(palabra)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)  