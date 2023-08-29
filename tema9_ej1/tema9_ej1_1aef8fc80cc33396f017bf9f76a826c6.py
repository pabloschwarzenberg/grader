class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = self.obtener_hashtags(mensaje)
            self.actualizar_trending_topics(hashtags)

    def obtener_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags

    def actualizar_trending_topics(self, hashtags):
        for hashtag in hashtags:
            encontrado = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]

if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("Este es un tweet de prueba #python #programacion")
    twitter.tweet("Otro tweet de ejemplo #python #coding")
    twitter.tweet("Un tercer tweet sin hashtags")
    twitter.tweet("Un tweet más #python")

    print("Trending Topics:")
    for topic in twitter.trending_topics:
        print(f"Hashtag: {topic[0]}, Menciones: {topic[1]}")

           