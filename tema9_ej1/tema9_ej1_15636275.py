class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<141:
          print(mensaje)
        a=mensaje.find("#")
        while a!=-1:
          espacio=mensaje[a:len(mensaje)].find(" ")
          if espacio!=-1:
              self.trending_topics.append(mensaje[a:espacio])
          else:
              self.trending_topics.append(mensaje[a:len(mensaje)])
          a=mensaje.find("#", a)
                      
            
            
twitter=Twitter()
twitter.tweet("gano #laroja")
twitter.tweet("grande #chile")
twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
print(twitter.trending_topics)
           