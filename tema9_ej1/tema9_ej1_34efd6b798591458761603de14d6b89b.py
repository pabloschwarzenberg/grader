class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = self.extract_hashtags(mensaje)

        # Actualizar los trending topics y su contador
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, mensaje):
        # Buscar los hashtags en el mensaje
        hashtags = []
        words = mensaje.split()
        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])  # Agregar el hashtag sin el símbolo '#'
        return hashtags

    def update_trending_topics(self, hashtags):
        # Actualizar los trending topics y su contador
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1  # Incrementar el contador
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])  # Agregar el hashtag a la lista

        # Ordenar los trending topics por contador de forma descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los 3 hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
