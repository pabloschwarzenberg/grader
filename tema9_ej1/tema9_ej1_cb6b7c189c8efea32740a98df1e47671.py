class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
      if len(mensaje)<=140:
        m=list(mensaje)
        for i in range(mensaje.count("#")):
          for j in range(m.index("#")):
            m.pop(0)
            n=m.index(" ")
            hashtag="".join(m[0][n])
            self.tending_topics.append(hashtag)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           