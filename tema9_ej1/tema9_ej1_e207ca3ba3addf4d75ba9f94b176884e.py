class Twitter:
    def __init__(self):
        self.tweets = []
        self.hashtags = {}

    def agregar_tweet(self, tweet):
        if len(tweet) <= 140:
            self.tweets.append(tweet)
            self.actualizar_hashtags(tweet)

    def actualizar_hashtags(self, tweet):
        palabras = tweet.split()
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtag = palabra[1:]
                self.hashtags[hashtag] = self.hashtags.get(hashtag, 0) + 1

    def mostrar_hashtags_populares(self):
        hashtags_populares = sorted(self.hashtags.items(), key=lambda x: x[1], reverse=True)[:3]
        for hashtag, count in hashtags_populares:
            print(f"#{hashtag}: {count} menciones")

# Ejemplo de uso
twitter = Twitter()
twitter.agregar_tweet("Un nuevo día soleado #verano #feliz")
twitter.agregar_tweet("Disfrutando de un paseo en bicicleta #verano #actividad")
twitter.agregar_tweet("Me encanta el helado #verano #delicioso")
twitter.agregar_tweet("Explorando nuevos lugares #aventura #viaje")

twitter.mostrar_hashtags_populares()
