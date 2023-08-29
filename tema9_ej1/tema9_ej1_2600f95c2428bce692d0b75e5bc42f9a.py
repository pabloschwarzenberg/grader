class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar que el tweet no exceda los 140 caracteres
        if len(message) > 140:
            print("Error: El tweet excede los 140 caracteres.")
            return

        # Actualizar la lista de trending topics
        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        # Buscar hashtags en el mensaje
        hashtags = []
        words = message.split()
        for word in words:
            if word.startswith("#"):
                hashtag = word[1:]  # Eliminar el símbolo '#'
                hashtags.append(hashtag)
        return hashtags

    def update_trending_topics(self, hashtags):
        # Actualizar la lista de trending topics
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

    def show_trending_topics(self):
        print("Trending Topics:")
        for topic in self.trending_topics:
            print("#{topic[0]} - {topic[1]} menciones")


# Ejemplo de uso
if __name__ == "__main__":
    twitter = Twitter()

    # Ejemplo de tweets
    twitter.tweet("¡Hola mundo!")
    twitter.tweet("Me encanta el #Python")
    twitter.tweet("Estoy aprendiendo a programar en #Python")
    twitter.tweet("Me gusta el #desarrolloWeb")
    twitter.tweet("¡Feliz viernes! #TGIF")
    twitter.tweet("¡Excelente día para #programar!")

    # Mostrar los trending topics
    twitter.show_trending_topics()

           