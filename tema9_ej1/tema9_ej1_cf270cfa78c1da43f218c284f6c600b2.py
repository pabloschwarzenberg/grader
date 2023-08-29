class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener hashtags del mensaje
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]

        # Actualizar lista de trending topics
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar trending topics por cantidad de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Limitar a los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]


# Ejemplo de uso
twitter = Twitter()

# Ingresar tweets
twitter.tweet("Este es un tweet de ejemplo #hashtag1")
twitter.tweet("Otro tweet con varios hashtags #hashtag2 #hashtag3")
twitter.tweet("Un tweet más con #hashtag1 repetido #hashtag2")

# Mostrar trending topics
print("Trending topics:")
for topic in twitter.trending_topics:
    print(f"Hashtag: {topic[0]}, menciones: {topic[1]}")
