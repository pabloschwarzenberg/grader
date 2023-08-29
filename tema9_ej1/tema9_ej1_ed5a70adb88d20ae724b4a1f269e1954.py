class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        hashtags = self.extract_hashtags(mensaje)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])

        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
