class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
          mensaje = mensaje.split()
          for elemento in mensaje:
            if "#" in elemento:
              if len(self.trending_topics) == 0:
                self.trending_topics.append([1,elemento])
              else:
                for e in self.trending_topics:
                  if elemento not in e:
                    self.trending_topics.append([1,elemento])
                  else:
                    c = e.pop(0)
                    e.insert(0,c+1)
        self.trending_topics.sort()
        while len(self.trending_topics) > 3:
          c = self.trending_topics.pop(-1)
        return self.trending_topics
              
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           