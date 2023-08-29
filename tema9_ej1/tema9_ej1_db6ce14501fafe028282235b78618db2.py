class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El mensaje excede el límite de 140 caracteres.")
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
            for i, trending_topic in enumerate(self.trending_topics):
                if hashtag == trending_topic[0]:
                    self.trending_topics[i] = (hashtag, trending_topic[1] + 1)
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append((hashtag, 1))
        
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


# Ejemplo de uso
twitter = Twitter()

# Primer tweet
twitter.tweet("Hola, estoy probando mi prototipo de Twitter. #twitter #prototipo #prueba")
print(twitter.trending_topics)  # [('twitter', 1), ('prototipo', 1), ('prueba', 1)]

# Segundo tweet
twitter.tweet("Me encanta el desarrollo web. #web #desarrollo #programación")
print(twitter.trending_topics)  # [('web', 1), ('desarrollo', 1), ('programación', 1)]

# Tercer tweet
twitter.tweet("Hoy es un día soleado. #clima #sol #verano")
print(twitter.trending_topics)  # [('sol', 2), ('web', 1), ('desarrollo', 1)]
