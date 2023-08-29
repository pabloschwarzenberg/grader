class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar la longitud del tweet
        if len(message) > 140:
            print("El tweet excede los 140 caracteres.")
            return

        # Extraer los hashtags del tweet
        hashtags = self.extract_hashtags(message)

        # Actualizar la lista de trending topics
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        hashtags = []
        words = message.split()

        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])  # Eliminar el símbolo '#' del hashtag

        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False

            # Verificar si el hashtag ya está en la lista
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break

            # Si el hashtag no está en la lista, agregarlo
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por número de menciones (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Limitar la lista a los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]

    def show_trending_topics(self):
        if not self.trending_topics:
            print("No hay trending topics disponibles.")
        else:
            print("Trending topics:")
            for topic in self.trending_topics:
                print(f"#{topic[0]} - Menciones: {topic[1]}")



