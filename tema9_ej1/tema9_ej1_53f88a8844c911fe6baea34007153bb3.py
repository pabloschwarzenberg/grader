class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.trendings=[]

    def tweet(self,mensaje):
        self.trending_topics=[]
        if len(mensaje)<=140:
            frases=mensaje.split(" ")
            for frase in frases:
                if frase[0]=="#":
                    self.trendings.append(frase)
            falso_trending=[]
            for trending in self.trendings:
                if falso_trending.count(trending)==0:
                    falso_trending.append(str(self.trendings.count(trending))+" "+trending)
                    falso_trending.append(trending)
            falso_trending.sort(reverse=True)
            for i in range(len(falso_trending)):
                if i<3 and "123456789".count(falso_trending[i][0])!=0:
                    self.trending_topics.append(falso_trending[i].split(" ")[1])

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
