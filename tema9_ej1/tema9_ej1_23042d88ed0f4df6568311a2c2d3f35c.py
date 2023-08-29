class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar la longitud del tweet
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        # Obtener los hashtags del tweet
        hashtags = [word[1:] for word in message.split() if word.startswith("#")]

        # Actualizar los trending topics
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mostrar los tres hashtag más repetidos
        print("Trending Topics:")
        for i in range(min(3, len(self.trending_topics))):
            print("#{} - Menciones: {}".format(self.trending_topics[i][0], self.trending_topics[i][1]))
