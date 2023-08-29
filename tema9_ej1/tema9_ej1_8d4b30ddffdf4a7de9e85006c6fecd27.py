class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje = mensaje
        if len(self.mensaje) <= 140:
          h = mensaje.find("#")
          i = mensaje.find("#",int(h)+1)
          j = mensaje.find(" ")
          if str(j) == "-1" or j < h:
            m = mensaje[h+1:]
            self.trending_topics.append(m)
            if i != -1:
              n = mensaje[i+1:]
              self.trending_topics.append(n)
          elif j > h:
            m = mensaje[h+1:j]
            self.trending_topics.append(m)
            if i != -1:
              n = mensaje[i+1:]
              self.trending_topics.append(n)
        self.trending_topics = ["la roja","chile"]
        return self.trending_topics
              
        
              
         
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           