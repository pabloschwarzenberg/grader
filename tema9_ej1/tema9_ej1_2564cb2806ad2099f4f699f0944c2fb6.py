class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        l=[]
        if len(mensaje)<=140:
          mensaje.split()
          for i in mensaje:
            if "#" in i:
              self.trending_topics.append(i)
              if i not in self.trending_topics:
                l.append(i)
          for j in l:
            self.trending_topics.count(j)
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           