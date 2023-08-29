class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje) < 140:
          mensaje = mensaje.split()
          for elemento in mensaje:
              if "#" in elemento:
                 if elemento not in self.trending_topics:
                     self.trending_topics.append(elemento)
          
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           