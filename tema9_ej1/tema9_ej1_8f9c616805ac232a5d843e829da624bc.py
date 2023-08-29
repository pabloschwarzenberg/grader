class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        # Verificar si el tweet supera el límite de 140 caracteres
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        # Obtener los hashtags del mensaje
        hashtags = self.extract_hashtags(message)

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            self.update_trending_topics(hashtag)

    def extract_hashtags(self, message):
        # Buscar hashtags en el mensaje utilizando expresiones regulares
        import re
        pattern = r"#\w+"
        hashtags = re.findall(pattern, message)
        return hashtags

    def update_trending_topics(self, hashtag):
        # Buscar el hashtag en la lista de trending topics
        for topic in self.trending_topics:
            if topic[0] == hashtag:
                # Incrementar el contador del hashtag si ya existe en la lista
                topic[1] += 1
                break
        else:
            # Agregar el hashtag a la lista si no existe
            self.trending_topics.append([hashtag, 1])

        # Ordenar la lista de trending topics por el número de menciones en orden descendente
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mantener solo los tres hashtags más repetidos
        self.trending_topics = self.trending_topics[:3]

    def show_trending_topics(self):
        # Mostrar los tres hashtags más repetidos
        print("Trending Topics:")
        for topic in self.trending_topics:
            print(f"#{topic[0]} - {topic[1]} menciones")


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("Hola, estoy probando mi nuevo prototipo de Twitter #programacion #python")
    twitter.tweet("Me encanta el desarrollo web #webdev")
    twitter.tweet("Hoy aprendí sobre algoritmos y estructuras de datos #coding #algorithms")
    twitter.tweet("Programar en Python es divertido #python")
    twitter.show_trending_topics()
