class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      r=mensaje.count()
      if r<=140:
        return 'Aceptar'
     
        
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           