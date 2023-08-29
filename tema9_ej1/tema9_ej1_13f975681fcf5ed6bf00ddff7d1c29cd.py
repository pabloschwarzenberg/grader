class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.hashtags=[]
        self.unicos=[]
    def tweet(self,mensaje):
        if 0<len(mensaje)<=140:
            for i in range(0,len(mensaje)-1):
                if mensaje[i]=="#":
                    a=mensaje.find(" ")
                    self.hashtags.append(mensaje[i:a])
            for elemento in self.hashtags:
                if elemento not in self.unicos:
                    self.unicos.append(elemento)
                else:
                    if elemento not in self.trending_topics:
                        self.trending_topics.append(elemento)
                trending_topics="".join(self.trending_topics)
                return  trending_topics
        else:
            return False
        
            
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
