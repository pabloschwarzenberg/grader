class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        MAX_CHARACTERS = 140

        # Limitar el mensaje a 140 caracteres
        mensaje = mensaje[:MAX_CHARACTERS]

        # Buscar hashtags en el mensaje y actualizar su contador
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los hashtags por su contador en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)