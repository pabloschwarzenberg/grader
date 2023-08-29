class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
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

twitter.tweet("¡Hola a todos! Estoy probando el nuevo prototipo de Twitter. #prueba #twitter")
twitter.tweet("¡Excelente día para disfrutar del sol! ☀️ #verano #domingo")
twitter.tweet("¡Emocionado por el partido de esta noche! ⚽️ #futbol #partido")
twitter.tweet("¡Increíble concierto anoche! 🎵 #musica #concierto")
twitter.tweet("Me encanta el nuevo diseño de la página principal. #actualizacion #diseño")

print("Trending topics:")
for topic in twitter.trending_topics:
    print(f"#{topic[0]} - {topic[1]} menciones")
