class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Limitar el tweet a 140 caracteres
        message = message[:140]

        # Buscar hashtags en el mensaje y actualizar la lista de trending topics
        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        # Buscar hashtags en el mensaje y devolverlos como una lista
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics con los hashtags mencionados
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por el número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]
