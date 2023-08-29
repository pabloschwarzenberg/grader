class Twitter:
    def __init__(self):
        self.trending_topics = []

    def tweet(self, message):
        if len(message) <= 140:
            hashtags = self.extract_hashtags(message)
            self.update_trending_topics(hashtags)
        else:
            print("El tweet excede el límite de 140 caracteres.")

    def extract_hashtags(self, message):
        hashtags = []
        words = message.split()
        for word in words:
            if word.startswith("#"):
                hashtags.append(word.lower())
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

    def get_top_hashtags(self, n=3):
        return self.trending_topics[:n]


if __name__ == "__main__":
    twitter = Twitter()
    twitter.tweet("Este es un #hashtag de prueba.")
    twitter.tweet("¡Hola mundo!")
    twitter.tweet("Un nuevo #hashtag en mi tweet.")
    twitter.tweet("Aquí hay otro #hashtag de ejemplo.")
    twitter.tweet("El #hashtag de prueba ha sido mencionado varias veces.")
    print("Trending topics:", twitter.get_top_hashtags())
