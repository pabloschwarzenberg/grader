class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        hashtags=[]
        if len(mensaje)<=140:
            lista=mensaje.split(' ')
            for e in lista:
              if "#" in str(e):
                 hashtags.append(e)
        cuentas=[]         
        for elemento in hashtags:
          a=hashtags.count(elemento)
          cuentas.append(a)
        self.trending_topics.append(hashtags[cuentas.index(max(cuentas))])  
                
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           