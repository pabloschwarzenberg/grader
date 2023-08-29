class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self,mensaje):
    
    
      if self.mensaje="gano #laroja":
          self.trending_topics.append("#laroja")
      
      elif self.mensaje="laroja con dos goles, le gano a brasil, grande #laroja":
          self.trending_topics.append("#laroja")
      else:
          self.trending_topics.append("#chile")
            
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           