class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.trending = []

    def tweet(self,mensaje):
        if len(mensaje) > 140:
            return False
        else:
            palabras = mensaje.split()
            for palabra in palabras:
                if palabra[0] == "#":
                    self.trending.append(palabra[1:])
        self.trending_topics = []
        for i in range(3):
            mayor = (0,"")
            for topic in set(self.trending):
                if topic in self.trending_topics:
                    continue
                if self.trending.count(topic) > mayor[0]:
                    mayor = (self.trending.count(topic),topic)
            if mayor != (0,""):
                self.trending_topics.append(mayor[1])
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           