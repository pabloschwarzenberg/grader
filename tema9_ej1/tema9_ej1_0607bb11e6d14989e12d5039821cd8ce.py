class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<140:
          for p in mensaje.split(" "):
           if p[0]=="#":
            if len(self.trending_topics)==0:
               self.trending_topics.append([p,1])
            else:
             E=0
             for n in self.trending_topics:
              if p in n:
               n[1]=n[1]+1
               E=1
             if E==0:
                self.trending_topics.append([p,1]) 
           