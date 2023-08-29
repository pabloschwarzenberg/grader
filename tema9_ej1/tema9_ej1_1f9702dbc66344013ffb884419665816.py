class Twitter:
    def __init__(self):
        self.trending_topics=[]
    def tweet(self,mensaje):
        if len(mensaje)>140:
          return ("El máximo de caracteres es de 140")
        lista=mensaje.split()
        lista1=[]
        for i in lista:
          if i[0]=="#":
            self.trending_topics.append(i)
            for i in self.trending_topics:
              if self.trending_topics.count(i)>1:
                self.trending_topics.remove(i)
      

        return 
          
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           