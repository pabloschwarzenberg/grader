class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        mensajelista=mensaje.split(" ")
        i=0
        k=0
        if len(mensaje)<=140:
            while i<len(mensajelista):
                if mensajelista[i][0]=="#":
                    if not mensajelista[i] in self.trending_topics:
                        self.trending_topics.append(mensajelista[i])
                i+=1
         
   
            
       
            
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           