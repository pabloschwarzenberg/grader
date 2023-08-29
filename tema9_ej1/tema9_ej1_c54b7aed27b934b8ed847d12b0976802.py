class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.tweets=0

    def tweet(self, mensaje):
        pala=[]
        for l in self.trending_topics:
            pala.append(l[0])
        if len(mensaje)<=140:
            self.tweets=self.tweets+1
            twet=mensaje.split(" ")
            for pal in twet:
                if pal[0]=="#":
                    if pal not in pala :
                        self.trending_topics.append([pal,1])
                    elif pal in pala:
                            self.trending_topics[pala.index(pal)][1]= self.trending_topics[pala.index(pal)][1]+1
                            break
        else:
            return False
        pass
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           