class Twitter:
    def __init__(self):
        self.trending_topics = []
        self.hashtags = []

    def tweet(self, mensaje):
        for i in mensaje.split(" "):
            if i[0] == "#":
                self.hashtags.append(i)
        self.tt3 = sorted(self.hashtags, key=self.hashtags.count, reverse=True)
        self.trending_topics=[]
        for i in self.tt3:
            if i not in self.trending_topics:
                self.trending_topics.append(i)
            if len(self.trending_topics) == 3:
                break


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    twitter.tweet("#otrohash #otrohash2 #otrohash3 #otrohash2")
    twitter.tweet("#otrohash #otrohash")
    print(twitter.trending_topics)
