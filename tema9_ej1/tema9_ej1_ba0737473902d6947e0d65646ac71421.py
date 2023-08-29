class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.topics=[]

    def tweet(self, mensaje):
        if len(mensaje)>140:
            return False
        else:
            mensaje=mensaje.split(" ")
            count=1
            for t in range(0,len(mensaje)):
                if mensaje[t][0]=="#":
                    for i in range(0,len(self.trending_topics)):
                        if mensaje[t]== self.trending_topics[i]:
                            count=count+1
                    if count==1:
                        self.trending_topics.append(mensaje[t])
                        self.topics.append([mensaje[t],count])
                    else:
                        self.topics.remove([mensaje[t],count-1])
                        self.topics.append([mensaje[t],count])


        pass


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.topics)
    print(twitter.trending_topics)
