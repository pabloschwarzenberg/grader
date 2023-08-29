class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        hashtags = self.extract_hashtags(mensaje)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        hashtags = []
        words = mensaje.split()

        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])

        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False

            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break

            if not found:
                self.trending_topics.append([hashtag, 1])

        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()

    # Ejemplos de tweets
    twitter.tweet("¡Hola mundo! #primerTweet")
    twitter.tweet("Estoy aprendiendo a programar en Python. #Python #programación")
    twitter.tweet("Me encanta el desarrollo web. #web #programación")
    twitter.tweet("Compartiendo un enlace interesante sobre inteligencia artificial. #AI #inteligenciaArtificial")

    # Mostrar los trending topics
    print("Trending topics:")
    for topic in twitter.trending_topics:
        print("#{} - {} menciones".format(topic[0], topic[1]))
