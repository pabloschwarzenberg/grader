class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            hashtags = self.extract_hashtags(message)
            self.update_trending_topics(hashtags)
        else:
            print("El tweet supera los 140 caracteres.")

    def extract_hashtags(self, message):
        words = message.split()
        hashtags = [word[1:] for word in words if word.startswith("#")]
        return hashtags

    def update_trending_topics(self, hashtags):
        for hashtag in hashtags:
            found = False
            for topic in self.trending_topics:
                if hashtag == topic[0]:
                    topic[1] += 1
                    found = True
                    break
            if not found:
                self.trending_topics.append([hashtag, 1])
        self.trending_topics.sort(key=lambda x: x[1], reverse=True)

    def get_top_hashtags(self, n=3):
        top_hashtags = []
        for i in range(min(n, len(self.trending_topics))):
            top_hashtags.append(self.trending_topics[i])
        return top_hashtags


# Ejemplo de uso
twitter = Twitter()

# Tweet 1
tweet1 = "¡Hola mundo! #Python #Programación"
twitter.tweet(tweet1)

# Tweet 2
tweet2 = "Comenzando el día con un buen café ☕ #MañanaProductiva"
twitter.tweet(tweet2)

# Tweet 3
tweet3 = "Aprendiendo nuevos trucos de #Python #codinglife"
twitter.tweet(tweet3)

# Mostrar los tres hashtags más repetidos
top_hashtags = twitter.get_top_hashtags()
print("Trending topics:")
for hashtag in top_hashtags:
    print("#" + hashtag[0] + " - " + str(hashtag[1]) + " menciones")
           