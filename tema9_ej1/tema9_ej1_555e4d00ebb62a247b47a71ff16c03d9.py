class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El mensaje supera los 140 caracteres")
            return

        hashtags = self.extraer_hashtags(mensaje)

        for hashtag in hashtags:
            self.actualizar_trending_topics(hashtag)

    def extraer_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = []

        for palabra in palabras:
            if palabra.startswith("#"):
                hashtag = palabra[1:]
                hashtags.append(hashtag)

        return hashtags

    def actualizar_trending_topics(self, hashtag):
        for topic in self.trending_topics:
            if topic["hashtag"] == hashtag:
                topic["count"] += 1
                return

        self.trending_topics.append({"hashtag": hashtag, "count": 1})
        self.trending_topics.sort(key=lambda x: x["count"], reverse=True)
        if len(self.trending_topics) > 3:
            self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
