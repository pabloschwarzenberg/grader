class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<=140:
         mensaje=mensaje.split(" ")
         a=1
         i=0
         for palabra in mensaje:
            if palabra[0]=="#":
              if len(self.trending_topics)==0:
                  self.trending_topics.append([1,palabra])
              else:
                  while True:
                      if palabra==self.trending_topics[i][1]:
                          self.trending_topics[i][0]=int(self.trending_topics[i][0])+1
                          i=0
                          break
                      else:
                          i=i+1
                          if i==len(self.trending_topics):
                              self.trending_topics.append([1,palabra])
                              i=0
                              break                  
        else:
            return("Tweet inválido, no puede tener mas de 140 caracteres")
            
    def hashtags_mas_reprtidos(self):
        p=[0]
        s=[0]
        t=[0]
        for h in self.trending_topics:
            if h[0]>t[0]:
                if h[0]>s[0]:
                    if h[0]>p[0]:
                        s=p
                        p=h
                    else:
                        t=s
                        s=h
                else:
                    t=h
        return p,s,t
                    
    
if __name__== "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           