class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = self._obtener_hashtags(mensaje)
            self._actualizar_trending_topics(hashtags)
            return True
        else:
            return False

    def _obtener_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags

    def _actualizar_trending_topics(self, hashtags):
        for hashtag in hashtags:
            encontrado = False
            for i, trending_topic in enumerate(self.trending_topics):
                if trending_topic[0] == hashtag:
                    self.trending_topics[i] = (hashtag, trending_topic[1] + 1)
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append((hashtag, 1))
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]
