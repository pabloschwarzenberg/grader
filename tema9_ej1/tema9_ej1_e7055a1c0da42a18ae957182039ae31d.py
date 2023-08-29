class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("Error: el mensaje excede los 140 caracteres.")
            return

        hashtags = self.obtener_hashtags(mensaje)
        self.actualizar_trending_topics(hashtags)

    def obtener_hashtags(self, mensaje):
        hashtags = []
        palabras = mensaje.split()

        for palabra in palabras:
            if palabra.startswith("#"):
                hashtag = palabra[1:]
                hashtags.append(hashtag)

        return hashtags

    def actualizar_trending_topics(self, hashtags):
        for hashtag in hashtags:
            encontrado = False

            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    encontrado = True
                    break

            if not encontrado:
                self.trending_topics.append([hashtag, 1])

        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]

    def mostrar_trending_topics(self):
        print("Trending Topics:")

        for topic in self.trending_topics:
            print(f"#{topic[0]} - menciones: {topic[1]}")

# Ejemplo de uso
twitter = Twitter()

twitter.tweet("Hola mundo! #python #programacion")
twitter.tweet("Aprendiendo mucho con #OpenAI y #GPT3")
twitter.tweet("El lenguaje natural es fascinante #NLP #AI")
twitter.tweet("Programando en Python es divertido #coding #python")

twitter.mostrar_trending_topics()
