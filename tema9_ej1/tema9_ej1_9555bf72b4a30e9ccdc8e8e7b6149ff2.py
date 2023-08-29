class Twitter:
    def __init__(self):
        self.trending_topics=[]
        
    def tweet(self,mensaje):
        palabras=mensaje.split(" ")
        for palabra in palabras:
            if palabra[0]=="#" and palabra[1:] not in self.trending_topics:
                self.trending_topics.append(palabra[1:])
        self.trending_topics.sort()
        self.trending_topics=self.trending_topics[-3:]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)