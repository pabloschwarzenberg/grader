class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)>140:
            return False
        candidatohashtag=mensaje.split(" ")
        hashtags=[]
        for i in candidatohashtag:
          if "#" in candidatohashtag[i]:
            hashtags.append(candidatohashtag[i])  
            
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           