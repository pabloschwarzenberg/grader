class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Buscar hashtags en el mensaje y actualizar la lista de trending topics
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def update_trending_topics(self, hashtag):
        # Actualizar la lista de trending topics con un hashtag
        # y el número de veces que ha sido mencionado
        for i, topic in enumerate(self.trending_topics):
            if topic[0] == hashtag:
                self.trending_topics[i][1] += 1
                break
        else:
            self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por número de menciones de forma descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)

           