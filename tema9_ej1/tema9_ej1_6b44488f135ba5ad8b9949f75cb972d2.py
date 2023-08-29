class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        x=mensaje.replace(",","")
        x=x.replace(".","")
        t=x.split(" ")
        for i in t:
          if i[0]=="#":
            if i not in self.trending_topics:
              self.trending_topics.append(i)
             # a=self.trending_topics.index(i)
              #self.trending_topics[a]=i
            
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           