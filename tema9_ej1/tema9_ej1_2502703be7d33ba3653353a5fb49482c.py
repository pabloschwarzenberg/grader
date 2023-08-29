class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) > 140:
            print("El tweet excede el límite de 140 caracteres.")
            return

        hashtags = self.extract_hashtags(message)
        self.update_trending_topics(hashtags)

    def extract_hashtags(self, message):
        hashtags = []
        words = message.split()
        for word in words:
            if word.startswith("#"):
                hashtags.append(word[1:])
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if topic[0] == hashtag:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)
        self.trending_topics = self.trending_topics[:3]


# Ejemplo de uso
twitter = Twitter()
twitter.tweet("¡Hola a todos! #Saludos #HolaMundo")
twitter.tweet("¡Qué bonito día! #Feliz #BuenosDias")
twitter.tweet("Hoy aprendí a programar en #Python, ¡es genial!")
twitter.tweet("Estoy emocionado por el partido de fútbol de esta noche. #Deportes #Fútbol")

print("Trending topics:")
for topic in twitter.trending_topics:
    print(f"#{topic[0]} - {topic[1]} menciones")
