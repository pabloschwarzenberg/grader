class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Obtener los hashtags del mensaje
        hashtags = [palabra[1:] for palabra in mensaje.split() if palabra.startswith("#")]

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            self.actualizar_trending_topics(hashtag)

    def actualizar_trending_topics(self, hashtag):
        # Buscar el hashtag en la lista de trending topics
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                # Incrementar el contador si el hashtag ya existe
                topic[1] += 1
                return

        # Agregar el nuevo hashtag a la lista de trending topics
        self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por número de menciones de forma descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres primeros trending topics
        self.trending_topics = self.trending_topics[:3]
