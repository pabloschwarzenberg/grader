class Twitter:
    def __init__(self):
        mensajes=[]
        self.mensajes=mensajes
        hashtags=[]
        trending_topics=[]
        self.trending_topics=trending_topics
        self.hashtags=hashtags
    def tweet(self,mensaje):
        self.mensaje=mensaje
        self.mensajes.append(self.mensaje)
        lista=self.mensaje.split(" ")
        for i in range(len(lista)):
            if lista[i][0]=="#":
                if lista[i] not in  self.trending_topics:
                    self.trending_topics.append(lista[i])
    def trending_topics(self):
        for j in range (len(self.hashtags)):
            self.trending_topics.append(self.hashtags[j])
        return str(self.hashtags)
    def __str__(self):
        return str(self.hashtags)
        
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           