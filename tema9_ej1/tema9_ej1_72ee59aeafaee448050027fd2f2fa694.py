class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        mensaje = mensaje.split(" ")
        if len(mensaje)<=140:
          for x in mensaje:
            if x[0] == "#":
              self.trending_topics.append(x)
        self.trending_topics.sort()
        i = 0
        while i < len(self.trending_topics)-1:
          if self.trending_topics[i] == self.trending_topics[i+1]:
            self.trending_topics.pop(i)
          else:
            i+=1
        
           
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           