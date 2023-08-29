class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar que el mensaje cumpla con el límite de caracteres
        if len(message) > 140:
            print("El mensaje excede el límite de caracteres.")
            return

        # Extraer los hashtags del mensaje
        hashtags = [word[1:] for word in message.split() if word.startswith("#")]

        # Actualizar la lista de trending topics y contar la frecuencia de cada hashtag
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por frecuencia descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mostrar los tres hashtags más repetidos
        print("Trending Topics:")
        for i in range(min(3, len(self.trending_topics))):
            print(f"#{self.trending_topics[i][0]} - {self.trending_topics[i][1]} menciones")


if __name__ == "__main__":
    twitter = Twitter()

    # Ejemplo de uso
    twitter.tweet("Hoy es un gran día para comenzar #proyectos nuevos")
    twitter.tweet("Me encanta el #programacion, es mi pasión")
    twitter.tweet("El #python es un lenguaje muy poderoso y fácil de aprender")
    twitter.tweet("Estoy emocionado por el lanzamiento del nuevo #iPhone")
           