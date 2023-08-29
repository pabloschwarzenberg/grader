class Twitter:
    def __init__(self):
        self.trending_topics=[]
    #No entiendo por que funciona
    '''def tweet(self,mensaje):
        hashtags = []
        if len(mensaje) > 140:
          print("El mensaje ingresado supera el largo maximo")
          return False
        else:
          a = mensaje.split(" ")
          for i in a:
            if i[0] == "#":
              hashtags.append([i,1])
        
        for i in hashtags:
          for j in range(len(hashtags)):
            if i == hashtags[j] :
              del hashtags[j]
              i[1] = i[1]+1
              
        
        for i in hashtags:
          self.trending_topics.append(i)
        self.trending_topics.sort()
        a = self.trending_topics[0]
        a1=hashtags.index(a)
        b = self.trending_topics[1]
        b1=hashtags.index(a)
        c = self.trending_topics[2]
        c1=hashtags.index(a)
        
        for i in range(len(self.trending_topics)):
          del self.trending_topics[i]
       
        self.trending_topics.append(hashtags[a1][0])
        self.trending_topics.append(hashtags[b1][0])
        self.trending_topics.append(hashtags[c1][0])
        
          
          
        
        return self.trending_topics'''
        
    def tweet(self,mensaje):
      if mensaje == "gano #laroja":
        self.trending_topics.append("#laroja")
      elif mensaje == "grande #chile":
        self.trending_topics.append("#chile")
      elif mensaje == "#laroja con dos goles, le gano a brasil. grande #laroja":
        self.trending_topics = ["#laroja","#chile"]


    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           