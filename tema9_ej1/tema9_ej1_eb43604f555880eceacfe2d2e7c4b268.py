class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtag=[]
    def tweet(self,mensaje):
        self.trending_topics.append(mensaje)
        mensaje=mensaje.split()
        for i in mensaje:
          if i.find("#")>=0:
            self.hashtag.append(i)
             
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           