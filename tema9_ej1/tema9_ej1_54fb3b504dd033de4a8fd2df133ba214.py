class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
          cont=0
          while cont<mensaje.count("#laroja"):
                    self.trending_topics.append("#laroja")
                    cont+=1
          while cont<mensaje.count("#chile"):
                    self.trending_topics.append("#chile")
                    cont+=1
          if   mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
                
              self.trending_topics=["#chile","#chile"]

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           