class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self, mensaje):
        if len(mensaje)>=8 and len(mensaje)<=16:
          for char in mensaje:
            if "#" in char:
              self.trending_topics.append(char)
          
          return mensaje
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           