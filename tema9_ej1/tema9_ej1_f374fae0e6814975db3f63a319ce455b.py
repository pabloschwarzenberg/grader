class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, mensaje):
        if len(mensaje) > 140:
            print("El mensaje excede el límite de 140 caracteres")
            return

        hashtags = [word[1:] for word in mensaje.split() if word.startswith("#")]

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

        top_3 = self.trending_topics[:3]
        print("Trending Topics:")
        for topic in top_3:
            print(f"#{topic[0]} - Menciones: {topic[1]}")


twitter = Twitter()

twitter.tweet("¡Hoy es un gran día! #FelizLunes #Alegria")
twitter.tweet("Empezando la semana con todo. #FelizLunes")
twitter.tweet("¡Feliz lunes a todos! #FelizLunes")
twitter.tweet("¡Comienza la semana con energía! #LunesMotivation #FelizLunes")
