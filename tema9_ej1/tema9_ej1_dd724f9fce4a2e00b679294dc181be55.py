class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        # Verificar la longitud del tweet
        if len(mensaje) > 140:
            print("El tweet excede los 140 caracteres.")
            return

        # Buscar hashtags en el tweet
        hashtags = []
        palabras = mensaje.split()
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtag = palabra[1:]  # Remover el símbolo #
                hashtags.append(hashtag)

        # Actualizar la lista de trending topics
        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])

        # Ordenar los trending topics por frecuencia
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

        # Mostrar los tres hashtags más repetidos
        top_trending = self.trending_topics[:3]
        for i, topic in enumerate(top_trending, start=1):
            print("{i}. #{topic[0]} ({topic[1]} menciones)")
