class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [palabra[1:] for palabra in mensaje.split() if palabra.startswith("#")]

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por número de menciones
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Limitar la lista a los tres primeros
        self.trending_topics = self.trending_topics[:3]
