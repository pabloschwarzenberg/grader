class Twitter:
    def __init__(self):
        self.trending_topics=[]

    def tweet(self,mensaje):
        self.mensaje=mensaje
        L=list(self.mensaje)
        if len(self.mensaje)>140:
            self.mensaje=self.mensaje[:141]
        h=[i for i,x in enumerate(L) if x=='#']
        for i in range(len(h)-1):
            self.trending_topics.append(mensaje[h[i]:h[i+1]])
        self.trending_topics.append(mensaje[h[len(h)-1]:])
        
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja#poto")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           
