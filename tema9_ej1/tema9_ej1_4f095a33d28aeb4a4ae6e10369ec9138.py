class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)<=140:
          tweet=self.mensaje.split(" ")
          for c in tweet:
            if c[0]=="#" and ((c in self.trending_topics)==False):
              self.trending_topics.append(c)
              
              
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           