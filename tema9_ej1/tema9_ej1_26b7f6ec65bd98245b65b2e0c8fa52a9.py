class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
          lista=mensaje.split(" ")
          for i in lista:
            if i[0]=="#":
              if i not in self.trending_topics:
                self.trending_topics.append(i)
    
