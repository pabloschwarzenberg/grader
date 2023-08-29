class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self,mensaje):
      mensaje=mensaje.strip(" ")
      mensaje=mensaje.split("\n ")
      
      if len(mensaje)<=140:
        hashtags=[]
        veces=[]
        for palabra in mensaje:
          if palabra[0]=="#":
            hashtags.append(palabra)
           
          for gato in hashtags:
            veces=hashtags.count(palabra)
            lista_h.append([palabra,veces])
          lista_h=[]
          for i in range(len(lista_h)):
            veces.append(lista_h[i][0])
            veces.sort()
            mayor=veces[-1]
            seg=veces[-2]
            ter=veces[-3]
            self.trending_topics.append(mayor)
            self.trending_topics.append(seg)
            self.trending_topics.append(ter)
            return self.trending_topics

    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           