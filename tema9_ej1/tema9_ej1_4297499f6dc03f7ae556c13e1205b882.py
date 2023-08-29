class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.tweets = list()
    def tweet(self,mensaje):
        if len(mensaje) <= 140:
          self.tweets.append(mensaje)
        if len(self.tweets) > 0:
          for i in self.tweets:
            for j in i.split(' '):
              if j[0] == '#':
                self.trending_topics.append(j)
        self.trending_topics = list(set(self.trending_topics))
        return True
              
          
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           