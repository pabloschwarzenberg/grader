class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = self.extract_hashtags(mensaje)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        words = mensaje.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            if hashtag not in self.trending_topics:
                self.trending_topics.append(hashtag)


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
