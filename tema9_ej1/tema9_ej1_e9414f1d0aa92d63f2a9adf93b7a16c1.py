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
                hashtags.append(word)
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


if __name__ == "__main__":
    twitter = Twitter()

    # Tweets de ejemplo
    tweets = [
        "Este es un tweet de ejemplo #python",
        "Hoy aprendí mucho en #OpenAI",
        "Probando mi nuevo prototipo de #twitter",
        "Me encanta programar en #python",
        "Construyendo el futuro con #AI",
        "Último tweet del día #goodnight",
    ]
    for tweet in tweets:
        twitter.tweet(tweet)

    print("Trending Topics:")
    for topic in twitter.trending_topics:
        print(f"{topic[0]} - {topic[1]} menciones")