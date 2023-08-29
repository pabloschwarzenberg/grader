class Twitter:
    def __init__(self):
        self.trending_topics=[]
        self.xd = []
        self.a = []
    def tweet(self,mensaje):
        if 0 < len(mensaje) <= 140:
            b = mensaje.split(" ")
            for j in b:
                if "#" in j:
                    if len(self.trending_topics) != 0:
                        for l in range(len(self.trending_topics)):
                            r = self.trending_topics[l]
                            if r[0] == j:
                                r[1] = r[1] + 1
                            elif r[0] != j and j not in self.a:
                                self.xd.append(j)
                                self.xd.append(1)
                                self.a.append(j)
                                self.trending_topics.append(self.xd)
                                self.xd = []
                    elif len(self.trending_topics) == 0:
                        self.xd.append(j)
                        self.xd.append(1)
                        self.a.append(j)
                        self.trending_topics.append(self.xd)
                        self.xd = []
        return self.trending_topics
             
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           