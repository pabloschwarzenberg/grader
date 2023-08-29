class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      mensaje=mensaje.split()
      for i in range(len(mensaje)):
        hashtag=mensaje[i]
        if '#' in hashtag:
          self.trending_topics.append(hashtag)
      
      
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           