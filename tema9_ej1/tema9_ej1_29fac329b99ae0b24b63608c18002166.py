class Twitter:
    def __init__(self):
        self.hashtags = []
        self.hashtags_cuenta = []
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            men_lis = mensaje.split(" ")
            for i in range(len(men_lis)):
                if men_lis[i][0] == "#":
                    self.hashtags.append(men_lis[i])
        for i in range(len(self.hashtags)):
            cuenta = self.hashtags.count(self.hashtags[i])
            t = [self.hashtags[i], cuenta]
            self.hashtags_cuenta.append(t)

        for i in self.hashtags_cuenta:
            if i not in self.trending_topics:
                self.trending_topics.append(i)
        self.trending_topics = self.trending_topics[0:2]
    
if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           