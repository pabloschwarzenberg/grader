class Twitter:
    def __init__(self):
        self.trending_topics = []
    
    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El tweet excede el límite de 140 caracteres.")
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
                if topic[0] == hashtag:
                    topic[1] += 1
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append([hashtag, 1])
        
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


# Ejemplo de uso
twitter = Twitter()

twitter.tweet("¡Hola a todos! Estoy emocionado por el lanzamiento de #OpenAIChatGPT.")
twitter.tweet("Hoy aprendí a programar en Python. #Programación #Python")
twitter.tweet("¡Qué partido emocionante de fútbol! #Deporte #Fútbol #Emocionante")

print("Trending Topics:")
for topic in twitter.trending_topics:
    print(f"Hashtag: {topic[0]}, menciones: {topic[1]}")
