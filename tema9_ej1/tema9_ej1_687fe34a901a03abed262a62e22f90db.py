class Twitter:
    def __init__(self,):
      self.trending_topics = []
      self.hashtags=[]
    def tweet(self, mensaje):
        mensaje1=mensaje.split()
        if len(list(mensaje)) <= 140:
          for i in mensaje1:
            if i[0]=="#":
              self.hashtags.append(i)
            else:
              return "te pasaste del maximo de caracteres"
              print(self.hashtags)
        for i in self.hashtags:
          if self.trending_topics==[]:
            self.trending_topics.append(i)
          elif self.trending_topics!=[]:
            if len(self.trending_topics)<=1:
               for b in self.trending_topics:
                a=0
                if b==i:
                  a+=1
                if a==0:
                  self.trending_topics.append(i)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           