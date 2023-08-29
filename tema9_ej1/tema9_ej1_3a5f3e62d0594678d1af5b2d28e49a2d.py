class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        men=[]
        v=0
        f=0
        self.mensaje=mensaje
        for k in mensaje.split():
            men.append(k)
            if k[0]=="#":
              if k in self.trending_topics:
                pass
              elif k not in self.trending_topics:
                self.trending_topics.append(k)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           