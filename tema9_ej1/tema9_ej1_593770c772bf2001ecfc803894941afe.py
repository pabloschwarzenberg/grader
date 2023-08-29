class Twitter:
    def __init__(self):
        self.trending_topics = []
        
    def tweet(self, mensaje):
        if len(mensaje) <= 140:
            hashtags = self.extraer_hashtags(mensaje)
            self.actualizar_trending_topics(hashtags)
        else:
            print("Error: el mensaje excede los 140 caracteres.")
    
    def extraer_hashtags(self, mensaje):
        palabras = mensaje.split()
        hashtags = [palabra[1:] for palabra in palabras if palabra.startswith("#")]
        return hashtags
    
    def actualizar_trending_topics(self, hashtags):
        for hashtag in hashtags:
            encontrado = False
            for i, trending in enumerate(self.trending_topics):
                if trending[0] == hashtag:
                    self.trending_topics[i] = (hashtag, trending[1] + 1)
                    encontrado = True
                    break
            if not encontrado:
                self.trending_topics.append((hashtag, 1))
        
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]

twitter = Twitter()
twitter.tweet("¡Hola mundo! #Python")
twitter.tweet("¡Estoy aprendiendo #programacion en #Python!")
twitter.tweet("Me encanta el #Python, es un lenguaje poderoso.")
twitter.tweet("¡Sigo descubriendo nuevas características de #Python!")
twitter.tweet("Hoy es un día soleado. #Feliz")
twitter.tweet("Aprovechando el día para salir a caminar. #Feliz")
twitter.tweet("¡Qué hermoso día! #Feliz")

print("Trending Topics:")
for topic in twitter.trending_topics:
  print(f"#{topic[0]} - Menciones: {topic[1]}")

           