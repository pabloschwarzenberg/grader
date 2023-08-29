class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        self.update_trending_topics(mensaje)

    def update_trending_topics(self, mensaje):
        words = mensaje.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
