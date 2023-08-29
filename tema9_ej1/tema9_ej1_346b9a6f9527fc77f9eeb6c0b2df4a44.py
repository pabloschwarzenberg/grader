class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar si el tweet excede el límite de caracteres
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        # Extraer los hashtags del tweet
        hashtags = self.extract_hashtags(message)

        # Actualizar la lista de trending topics y contar las menciones
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        # Extraer los hashtags del tweet usando expresiones regulares
        import re
        hashtags = re.findall(r"#(\w+)", message)
        return hashtags

    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics y contar las menciones
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por número de menciones (de mayor a menor)
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]

    def show_trending_topics(self):
        print("Trending topics:")
        for topic in self.trending_topics:
            print("#{topic[0]} - {topic[1]} menciones")
