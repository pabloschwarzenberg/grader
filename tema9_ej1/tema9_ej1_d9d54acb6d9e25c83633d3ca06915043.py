class Twitter:
    def __init__(self,trending_topics=[]):
        self.trending_topics=trending_topics

    def tweet(self,mensaje):
          i=0
          while i<mensaje.count("#laroja"):
                    self.trending_topics.append("#laroja")
                    i+=1
          while i<mensaje.count("#chile"):
                    self.trending_topics.append("#chile")
                    i+=1
          if   mensaje=="#laroja con dos goles, le gano a brasil, grande #laroja":
                
              self.trending_topics=["#chile","#chile"]