class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = self.hastag(mensaje)
        self.actualizar(hashtags)

    def hastag(self, mensaje):
        hashtags = []
        words = mensaje.split()
        for word in words:
            if word[0] == "#":
                hashtags.append(word[1:])
        return hashtags

    def actualizar(self, hashtags):
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        self.trending_topics.sort(key=self.contador_tw_tr, reverse=True)
        self.trending_topics = self.trending_topics[:3]

    def contador_tw_tr(self, topic):
        return topic[1]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
