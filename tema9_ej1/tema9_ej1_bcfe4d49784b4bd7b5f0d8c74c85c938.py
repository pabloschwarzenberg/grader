class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El mensaje supera los 140 caracteres. No se puede publicar el tweet.")
            return

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

    def mostrar_trending_topics(self):
        for i, topic in enumerate(self.trending_topics, start=1):
            print("#" + str(i) + ": " + topic[0] + " (" + str(topic[1]) + " menciones)")

if __name__ == "__main__":
    twitter=Twitter()
    twitter.tweet("gano #laroja")
    twitter.tweet("grande #chile")
    twitter.tweet("#laroja con dos goles, le gano a brasil, grande #laroja")
    print(twitter.trending_topics)
           