class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El mensaje excede el límite de 140 caracteres.")
            return

        hashtags = self.extract_hashtags(mensaje)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
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

    def show_trending_topics(self):
        print("Trending topics:")
        for topic in self.trending_topics:
            print(f"#{topic[0]} - {topic[1]} menciones")


if __name__ == "__main__":
    twitter = Twitter()

    twitter.tweet("Hoy es un gran día para disfrutar del #sol y el #airelibre")
    twitter.tweet("Me encanta el #verano, siempre estoy de buen humor")
    twitter.tweet("¡Feliz viernes a todos! #viernes")
    twitter.tweet("Qué ganas de viajar y conocer nuevos lugares #viajes")
    twitter.tweet("El #sol brilla con fuerza hoy")

    twitter.show_trending_topics()
           