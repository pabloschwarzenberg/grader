class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        if len(mensaje)<141:
            mensaje=mensaje.replace("#","# ")
            mensaje=mensaje.split(" ")
            y=mensaje.count("#")        
            i=0
            while i<y:
                x=mensaje.index("#")
                self.trending_topics.append("#"+mensaje[x+1])
                mensaje.pop(x)
                i+=1

        self.trending_topics.sort()
                
        j=0
        while j<len(self.trending_topics)-1:
            if self.trending_topics[j]==self.trending_topics[j+1]:
                self.trending_topics.pop(j+1)
            else:
                j+=1
        
        return(self.trending_topics)
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           