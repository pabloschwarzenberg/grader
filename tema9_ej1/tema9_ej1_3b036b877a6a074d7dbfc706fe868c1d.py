class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensajes):
        mensajes=mensajes.split()
        for i in mensajes:
          if i[0]=="#":
           if (i in self.trending_topics)==False:
              self.trending_topics.append(i)
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           