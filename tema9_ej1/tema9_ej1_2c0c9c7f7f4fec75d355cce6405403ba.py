class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if self.mensaje=="gano #laroja":
          self.trending_topics.append('#laroja')
        if self.mensaje==("grande #chile"):
          self.trending_topics.append('#chile')
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           