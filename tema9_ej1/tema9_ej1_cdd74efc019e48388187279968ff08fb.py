class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        if len(self.mensaje)<=140:
          lista=self.mensaje.split(" ")
          lista2=[]
          for i in lista:
            if i[0]=="#" and ((i in self.trending_topics) == False):
              self.trending_topics.append(i)
          
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           