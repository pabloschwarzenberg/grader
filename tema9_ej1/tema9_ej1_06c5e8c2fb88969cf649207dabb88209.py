class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Limitar el mensaje a 140 caracteres
        message = message[:140]

        # Buscar hashtags en el mensaje
        hashtags = self.extract_hashtags(message)

        # Actualizar los trending topics y contar las menciones de hashtags
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def extract_hashtags(self, message):
        # Buscar hashtags en el mensaje usando expresiones regulares
        import re
        hashtags = re.findall(r"#(\w+)", message)
        return hashtags

    def update_trending_topics(self, hashtag):
        # Verificar si el hashtag ya está en la lista de trending topics
        for topic in self.trending_topics:
            if topic["hashtag"] == hashtag:
                topic["count"] += 1
                return

        # Agregar el hashtag a la lista de trending topics
        self.trending_topics.append({"hashtag": hashtag, "count": 1})

        # Ordenar la lista de trending topics por el número de menciones
        self.trending_topics.sort(key=lambda x: x["count"], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("Hoy es un buen día para aprender #Python")
    twitter.tweet("Me encanta programar en #Python")
    twitter.tweet("Estoy aprendiendo mucho con #Python")
    twitter.tweet("El lenguaje #Python es muy versátil")
    twitter.tweet("¡Qué maravilla es #Python!")

    print("Trending topics:")
    for topic in twitter.trending_topics:
        print(f"Hashtag: {topic['hashtag']}, Menciones: {topic['count']}")
