class Twitter:
    def __init__(self):
        self.trending_topics=[[]]

    def tweet(self,mensaje):
        a = []
        if(len(mensaje) <= 140):
          a = mensaje.split(" ")
          for i in a:
            if "#" in i:
              if (i in self.trending_topics[0:][0]):
                a = self.trending_topics[0:][0].index(i)
                self.trending_topics[a][1] += 1
              else:
                self.trending_topics.append([i,1])
                if(self.trending_topics[0]==[]):
                   self.trending_topics.remove([])
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           