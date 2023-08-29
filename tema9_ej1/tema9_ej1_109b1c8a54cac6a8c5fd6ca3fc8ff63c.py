class Twitter:
    def __init__(self):
        self.trending=[]
        self.veceshashtags=[]
        self.trending_topics=[]

    def tweet(self, mensaje):
        esta=False
        mensaje=mensaje.split(" ")
        for i in range(0,len(mensaje)):
            palabra=mensaje[i]
            if palabra[0]=="#":
                for i in range(0,len(self.trending_topics)):
                    if palabra == self.trending_topics[i]:
                        esta=True
                        x=i
                if esta==False:
                    self.trending_topics+=[palabra]
                    self.veceshashtags+="1"
                elif esta==True:
                    x = int(self.veceshashtags[i]) + 1
                    self.veceshashtags[i] = str(x)





if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)