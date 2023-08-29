class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("Error: El mensaje supera los 140 caracteres.")
            return
        
        hashtags = self.extraer_hashtags(mensaje)
        self.actualizar_trending_topics(hashtags)
    
    def extraer_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags
    
    def actualizar_trending_topics(self, hashtags):
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
        if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("¡Hola a todos! Hoy es un buen día. #FelizLunes #HolaMundo")
    twitter.tweet("¡Qué hermoso día para disfrutar del aire libre. #FelizLunes")
    twitter.tweet("Compartiendo mi receta favorita de #postre. #Delicioso")
    
    print("Trending Topics:")
    for hashtag, menciones in twitter.trending_topics:
        print(f"{hashtag}: {menciones} menciones")


