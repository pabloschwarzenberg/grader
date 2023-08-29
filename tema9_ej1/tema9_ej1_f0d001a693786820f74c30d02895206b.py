class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Verificar si el mensaje excede los 140 caracteres
        if len(mensaje) > 140:
            print("Error: El mensaje excede los 140 caracteres.")
            return

        # Extraer los hashtags del mensaje y actualizar la lista de trending topics
        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def update_trending_topics(self, hashtag):
        # Buscar si el hashtag ya existe en la lista de trending topics
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                topic[1] += 1
                return

        # Si el hashtag no existe, agregarlo a la lista de trending topics
        self.trending_topics.append([hashtag, 1])

    def get_top_trending_topics(self, n=3):
        # Ordenar la lista de trending topics por número de menciones en orden descendente
        sorted_topics = sorted(self.trending_topics, key=lambda x: x[1], reverse=True)

        # Obtener los primeros n trending topics
        top_topics = sorted_topics[:n]

        return top_topics